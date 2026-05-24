from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # 🔥 NOVAS ROTAS
    path('delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),
    path('toggle/<int:assignment_id>/', views.toggle_complete, name='toggle_complete'),
]