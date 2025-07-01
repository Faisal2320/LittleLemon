from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} on {self.booking_date}"


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99999)]
    )

    def __str__(self):
        return f"{self.title} : {self.price}"
