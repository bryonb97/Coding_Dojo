from django.db import models

# Notes:
# Everytime you make a change to your models you need to run python manage.py makemigrations then python manage.py migrate!

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary = models.TextField(blank = True, null = False)
    featured = models.BooleanField(default = False) # null = True, default = True