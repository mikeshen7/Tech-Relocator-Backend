from django.test import TestCase
from django.urls import reverse

from .models import Job

class JobTests(TestCase):
    def setUp(self):
        self.test_job = Job.objects.create(
            id=0,
            title='Pandora',
            lat=999,
            lon=998,
            location='Naboo',
            employment_type='Jedi',
            industry='peace',
            job_function='badass',
            senority='master',
            education='otj',
            months_experience=5,
            salary_high=100,
            salary_low=0,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.test_job), "Pandora")

    def test_job_content(self):
        actual_title = self.test_job.title
        actual_lat = self.test_job.lat
        actual_lon = self.test_job.lon
        actual_location = self.test_job.location
        actual_employment_type = self.test_job.employment_type
        actual_industry = self.test_job.industry
        actual_job_function = self.test_job.job_function
        actual_senority = self.test_job.senority
        actual_education = self.test_job.education
        actual_months_experience = self.test_job.months_experience
        actual_salary_high = self.test_job.salary_high
        actual_salary_low = self.test_job.salary_low

        self.assertEqual(actual_title, 'Pandora')
        self.assertEqual(actual_lat, 999)
        self.assertEqual(actual_lon, 998)
        self.assertEqual(actual_location, 'Naboo')
        self.assertEqual(actual_employment_type, 'Jedi')
        self.assertEqual(actual_industry, 'peace')
        self.assertEqual(actual_job_function, 'badass')
        self.assertEqual(actual_senority, 'master')
        self.assertEqual(actual_education, 'otj')
        self.assertEqual(actual_months_experience, 5)
        self.assertEqual(actual_salary_high, 100)
        self.assertEqual(actual_salary_low, 0)

    def test_job_list_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/job_data/?salary=400000")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Machine Learning Engineer V")


    def test_job_detail_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/job_data/6037")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software Engineer - Developer Experience")

    def test_job_search(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/job_data/?title=data&location=seattle&salary=100000")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software Data Engineer, Analytics - Apple Media Products")
