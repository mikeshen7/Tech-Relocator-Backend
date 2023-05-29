from django.test import TestCase
from django.urls import reverse

from .models import Col

class ColTests(TestCase):
    def setUp(self):
        self.test_col = Col.objects.create(
            id=0,
            rank=999,
            state='Pandora',
            index=998,
            grocery=997,
            housing=996,
            utilities=995,
            transportation=994,
            health=993,
            misc=992,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.test_col), "Pandora")

    def test_col_content(self):
        actual_rank = self.test_col.rank
        actual_state = self.test_col.state
        actual_index = self.test_col.index
        actual_grocery = self.test_col.grocery
        actual_housing = self.test_col.housing
        actual_utilities = self.test_col.utilities
        actual_transportation = self.test_col.transportation
        actual_health = self.test_col.health
        actual_misc = self.test_col.misc

        self.assertEqual(actual_rank, 999)
        self.assertEqual(actual_state, 'Pandora')
        self.assertEqual(actual_index, 998)
        self.assertEqual(actual_grocery, 997)
        self.assertEqual(actual_housing, 996)
        self.assertEqual(actual_utilities, 995)
        self.assertEqual(actual_transportation, 994)
        self.assertEqual(actual_health, 993)
        self.assertEqual(actual_misc, 992)

    def test_col_list_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/col/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Washington")

    def test_col_detail_view(self):
        response = self.client.get("https://tech-relocator-backend.vercel.app/api/v1/col/?state=washington")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Washington")

    def test_no_response(self):
        no_response = self.client.get("/100000/")
        self.assertEqual(no_response.status_code, 404)
