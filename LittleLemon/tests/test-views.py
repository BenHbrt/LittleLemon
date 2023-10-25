from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Coffee", price=20, inventory=200)
        Menu.objects.create(title="Cola", price=15, inventory=340)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_menuItems = menuSerializer(items, many=True)
        self.assertEqual(serialized_menuItems.data, [
            {"title": "IceCream", "price": 80, "inventory": 100},
            {"title": "Coffee", "price": 20, "inventory": 200},
            {"title": "Cola", "price": 15, "inventory": 340}
        ])