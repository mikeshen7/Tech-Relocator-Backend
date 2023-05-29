from django.test import TestCase
from django.urls import reverse

from .models import Skill

class SkillTests(TestCase):
    def setUp(self):
        self.test_skill = Skill.objects.create(
            id=0,
            title="Jedi",
            skills=['mind tricks', 'light saber'],
        )

    def test_string_representation(self):
        self.assertEqual(str(self.test_skill), "Jedi")

    def test_skills_content(self):
        actual_title = self.test_skill.title
        actual_skills = self.test_skill.skills[0]

        self.assertEqual(actual_title, 'Jedi')
        self.assertEqual(actual_skills, 'mind tricks')

    def test_skills_list_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/skills/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technical Sales Executive -mumbai")

    def test_skills_detail_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/skills/462")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Technical Sales Executive -mumbai")

    def test_skills_search(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/skills/?search=python")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "microstrategy")
