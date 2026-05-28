from django.test import TestCase
from django.contrib.auth.models import User
from .models import Assignment


class AssignmentModelTest(TestCase):

    # Test assignment title
    def test_assignment_title(self):

        user = User.objects.create_user(
            username='testuser',
            password='12345'
        )

        assignment = Assignment.objects.create(
            user=user,
            title='Math Homework',
            description='Complete exercises'
        )

        self.assertEqual(
            assignment.title,
            'Math Homework'
        )

    # Test assignment string method
    def test_assignment_string(self):

        user = User.objects.create_user(
            username='testuser2',
            password='12345'
        )

        assignment = Assignment.objects.create(
            user=user,
            title='Science Project',
            description='Build volcano'
        )

        self.assertEqual(
            str(assignment),
            assignment.title
        )


class AssignmentViewTest(TestCase):

    # Test homepage status code
    def test_homepage_status_code(self):

        response = self.client.get('/')

        self.assertEqual(
            response.status_code,
            200
        )

    # Test logged in user
    def test_logged_in_user(self):

        user = User.objects.create_user(
            username='beatriz',
            password='12345'
        )

        login = self.client.login(
            username='beatriz',
            password='12345'
        )

        self.assertTrue(login)

    # Test assignment creation
    def test_create_assignment(self):

        user = User.objects.create_user(
            username='student',
            password='12345'
        )

        assignment = Assignment.objects.create(
            user=user,
            title='Essay',
            description='Write essay'
        )

        self.assertEqual(
            Assignment.objects.count(),
            1
        )