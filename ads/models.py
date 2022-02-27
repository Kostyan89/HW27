from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(null=True)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
