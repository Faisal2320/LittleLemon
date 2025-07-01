from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking
from django.contrib.auth.models import User


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date"]


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]
