from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ('appetizers', 'Appetizers'),
    ('breads', 'Breads'),
    ('soups_salads', 'Soups and Salads'),
    ('chicken', 'Chicken specials'),
    ('seafood', 'Seafood'),
    ('biryani', 'Biryani'),
    ('desserts', 'Desserts'),
    ('beverages', 'Beverages')
)

STATUS = (
    (0, 'Not Available'),
    (1, 'Available')
)


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
