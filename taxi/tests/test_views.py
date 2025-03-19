from django.test import TestCase, Client
from django.urls import reverse
from taxi.models import Client as TaxiClient, Driver, Order
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client_detail_url = reverse('client_detail', args=[4])
        self.client1 = TaxiClient.objects.create(
            id=4,
            name='test1',
            surname='test1',
            phone_number='test1'
        )

        self.driver_detail_url = reverse('driver_detail', args=[4])
        self.driver1 = Driver.objects.create(
            id=4,
            name='test1',
            surname='test1',
            phone_number='test1',
            license_number='test1',
            rating=2.0
        )

        self.order_detail_url = reverse('order_detail', args=[4])
        self.order1 = Order.objects.create(
            id=4,
            start_address='test1',
            final_address='test1',
            driver_id=self.driver1,
            km=7.0
        )
        self.order1.clients.set([self.client1.id])

    def test_client_list_GET(self):
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)

    def test_client_list_POST(self):
        data = {
                'id': 5,
                'name': 'new test name',
                'surname': 'new test surname',
                'phone_number': 'new test phone'
        }
        response = self.client.post(reverse('client_list'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_client_detail_GET(self):
        response = self.client.get(self.client_detail_url)
        self.assertEquals(response.status_code, 200)

    def test_client_detail_DELETE(self):
        response = self.client.delete(self.client_detail_url)
        self.assertEqual(response.status_code, 204)

    def test_client_detail_PUT(self):
        updated_data = {
            'id': 5,
            'name': 'updated test name',
            'surname': 'updated test surname',
            'phone_number': 'updated test phone'
        }
        response = self.client.put(self.client_detail_url, data=json.dumps(updated_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_driver_list_GET(self):
        response = self.client.get(reverse('driver_list'))
        self.assertEqual(response.status_code, 200)

    def test_driver_list_POST(self):
        data = {
                'id': 5,
                'name': 'new test name',
                'surname': 'new test surname',
                'phone_number': 'new test phone',
                'license_number': 'new test license',
                'rating': 2.0
        }
        response = self.client.post(reverse('driver_list'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_driver_detail_GET(self):
        response = self.client.get(self.driver_detail_url)
        self.assertEquals(response.status_code, 200)

    def test_driver_detail_DELETE(self):
        response = self.client.delete(self.driver_detail_url)
        self.assertEqual(response.status_code, 204)

    def test_driver_detail_PUT(self):
        updated_data = {
            'id': 5,
            'name': 'updated test name',
            'surname': 'updated test surname',
            'phone_number': 'updated test phone',
            'license_number': 'updated test license',
            'rating': 3.0
        }
        response = self.client.put(self.driver_detail_url, data=json.dumps(updated_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_order_list_GET(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)

    def test_order_list_POST(self):
        data = {
            'id': 5,
            'start_address': 'test1',
            'final_address': 'test1',
            'driver_id': self.driver1.id,
            'clients': [self.client1.id],
            'km': 7.0
        }
        response = self.client.post(reverse('order_list'), data=json.dumps(data), content_type='application/json')
        print(response.content)
        self.assertEqual(response.status_code, 201)

    def test_order_detail_GET(self):
        response = self.client.get(self.order_detail_url)
        self.assertEquals(response.status_code, 200)

    def test_order_detail_DELETE(self):
        response = self.client.delete(self.order_detail_url)
        self.assertEqual(response.status_code, 204)

    def test_order_detail_PUT(self):
        updated_data = {
            'id': 5,
            'start_address': 'updated test1',
            'final_address': 'updated test1',
            'driver_id': self.driver1.id,
            'clients': [self.client1.id],
            'km': 7.5
        }
        response = self.client.put(self.order_detail_url, data=json.dumps(updated_data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)




