from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class homeTests(TestCase):
    def test_home_view_status_code(self):
        url=reverse('home')
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
