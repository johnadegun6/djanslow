from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from models import Customer
from django.urls import reverse

# Create your tests here.


class SimpleTest(APITestCase):
    def setUp(self) -> None:
        self.CLIENT=APIClient()
      
    
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
        self.assertTrue(response.status_code, 201)

    


