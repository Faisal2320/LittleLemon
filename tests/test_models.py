from django.test import TestCase
from restaurant.models import MenuItem, Booking


class MenuItemTest(TestCase):

    def test_get_item(self):
        item = MenuItem.objects.create(title="ice-cream", price=12.99, inventory=180)
        self.assertEqual(str(item), "ice-cream : 12.99")
