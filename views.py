from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Assignment


# Home page
def index(request):

    # Criar assignment (somente logado)
    if request.method == "POST" and request.user.is_authenticated:

        title = request.POST["title"]
        description = request.POST["description"]

        Assignment.objects.create(
            user=request.user,
            title=title,
            description=description
        )

        return redirect('index')

    # Listar apenas assignments do usuário logado
    assignments = Assignment.objects.filter(user=request.user).order_by('completed') if request.user.is_authenticated else []

    return render(request, 'planner/index.html', {
        'assignments': assignments
    })


# Deletar assignment
def delete_assignment(request, assignment_id):

    assignment = get_object_or_404(Assignment, id=assignment_id)

    if assignment.user == request.user:
        assignment.delete()

    return redirect('index')


# Marcar como concluído / não concluído
def toggle_complete(request, assignment_id):

    assignment = get_object_or_404(Assignment, id=assignment_id)

    if assignment.user == request.user:
        assignment.completed = not assignment.completed
        assignment.save()

    return redirect('index')


# Register
def register_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        return redirect('index')

    return render(request, 'planner/register.html')


# Login
def login_view(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, 'planner/login.html')


# Logout
def logout_view(request):
    logout(request)
    return redirect('index')