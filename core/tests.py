from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import sys
# from models import Customer


# Create your tests here.


class SimpleTest(APITestCase):
    def setUp(self) -> None:
        self.Client=APIClient()
      
    
    # def test_true(self):
    #     self.assertEqual(1, 1)

    
    # def test_response(self):
    #     # res = self.client.post(self.path)
    #     self.assertEqual(200, 200)


    def test_assert_into_db(self):
        client = APIClient()
        path = reverse('add')
        payload = {'name':'Kio rant', 'sex':'Female', 'address': 'Ademuno'}
        response = client.post(path, payload)
        # self.path= reverse('home')
        # customer = Customer.objects.create('Kio rant', 'Female', '23 june')
        # customer.save()
        print(response.status_code, path)
        self.assertTrue(response, 200)

