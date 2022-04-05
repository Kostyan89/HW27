from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5)], null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=210, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    description = models.TextField(null=True)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="media/", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-price"]

    def __str__(self):
        return self.name


class Compilation(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
