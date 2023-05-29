from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import User_Profile

class UserProfileTests(TestCase):
    def setUp(self):
        self.testuser1 = get_user_model().objects.create_user(username='testuser1', email='testuser1@gmail.com', password='pass')

        self.test_user_profile = User_Profile.objects.create(
            id=12345,
            username=self.testuser1,
            title='Jedi',
            location='Naboo',
            desired_location='Corusant',
            desired_salary=999,
            experience=99,
            skills='light saber',
            saved_locations='none',
        )

    def test_col_content(self):
        actual_title = self.test_user_profile.title
        actual_location = self.test_user_profile.location
        actual_desired_location = self.test_user_profile.desired_location
        actual_desired_salary = self.test_user_profile.desired_salary
        actual_experience = self.test_user_profile.experience
        actual_skills = self.test_user_profile.skills
        actual_saved_locations = self.test_user_profile.saved_locations

        self.assertEqual(actual_title, 'Jedi')
        self.assertEqual(actual_location, 'Naboo')
        self.assertEqual(actual_desired_location, 'Corusant')
        self.assertEqual(actual_desired_salary, 999)
        self.assertEqual(actual_experience, 99)
        self.assertEqual(actual_skills, 'light saber')
        self.assertEqual(actual_saved_locations, 'none')

    def test_skills_list_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/users/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title from thunderclient")

    def test_skills_detail_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/users/3")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test title from thunderclient")
