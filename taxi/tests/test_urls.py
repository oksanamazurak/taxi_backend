from django.test import SimpleTestCase
from django.urls import reverse, resolve
from taxi.views import client_list, client_detail, driver_list, driver_detail, order_list, order_detail

class TestUrls(SimpleTestCase):

    def test_client_list_url_resolves(self):
        url = reverse('client_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, client_list)

    def test_client_detail_url_resolves(self):
        url = reverse('client_detail', kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, client_detail)

    def test_driver_list_url_resolves(self):
        url = reverse('driver_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, driver_list)

    def test_driver_detail_url_resolves(self):
        url = reverse('driver_detail', kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, driver_detail)

    def test_order_list_url_resolves(self):
        url = reverse('order_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_list)

    def test_order_detail_url_resolves(self):
        url = reverse('order_detail', kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_detail)