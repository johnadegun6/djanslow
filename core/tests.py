from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
# from models import Customer
from django.urls import reverse

# Create your tests here.


class SimpleTest(APITestCase):
    def setUp(self) -> None:
        self.CLIENT=APIClient()
        self.path= reverse('home')

    
    def test_true(self):
        self.assertEqual(1, 1)

    
    def test_response(self):
        # res = self.client.post(self.path)
        self.assertEqual(200, 200)


