from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=40)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name


class User(AbstractUser):
    HR = "hr"
    EMPLOYEE = "employee"
    UNKNOWN = "unknown"
    ROLES = [
        (HR, "hr"),
        (EMPLOYEE, "employee"),
        (UNKNOWN, "unknown"),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=9, choices=ROLES, default=UNKNOWN)
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
