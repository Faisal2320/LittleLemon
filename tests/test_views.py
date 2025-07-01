from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.99, inventory=10)
        self.item2 = MenuItem.objects.create(title="Burger", price=9.99, inventory=20)
        self.item3 = MenuItem.objects.create(title="Salad", price=7.99, inventory=15)

    def test_getall(self):
        response = self.client.get(reverse("menu-items"))  # adjust if URL name differs
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
