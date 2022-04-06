from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta

USER_AGE_MIN = 9


def check_birth_date(value: date):
    difference_in_years = relativedelta(date.today(), value).years
    if difference_in_years < USER_AGE_MIN:
        raise ValidationError(
            '%(value)s too small',
            params={'value':value}
        )


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
    ROLE = [
        (HR, "hr"),
        (EMPLOYEE, "employee"),
        (UNKNOWN, "unknown"),
    ]

    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=100, choices=ROLE, default=UNKNOWN)
    age = models.PositiveIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(Location, null=True, blank=True)
    birth_date = models.DateField(null=True, validators=[check_birth_date])
    email = models.EmailField(null=True, unique=True, blank=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
