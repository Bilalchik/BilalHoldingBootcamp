from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=223)

    def __str__(self):
        return self.title


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=123)
    model = models.CharField(max_length=123)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    year = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/car_images', blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.title
