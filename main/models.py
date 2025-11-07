
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class FordRental(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    car_model = models.CharField(max_length=100)
    rental_date = models.DateField()  # важливо!
    rental_duration = models.IntegerField()
    payment_method = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.car_model}"



class Car(models.Model):
    make = models.CharField(max_length=50)  # Марка
    model = models.CharField(max_length=50)  # Модель
    year = models.IntegerField()  # Рік виробництва
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна
    description = models.TextField()  # Опис
    popularity = models.IntegerField(default=0)  # Рейтинг популярності
    image = models.ImageField(upload_to='car_images/')  # Фото

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"




class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Клієнт (опціонально)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Автомобіль
    quantity = models.PositiveIntegerField(default=1)  # Кількість
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return f"Order by {self.customer} for {self.car}"


class Purchase(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Клієнт (опціонально)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)  # Автомобіль
    quantity = models.PositiveIntegerField(default=1)  # Кількість
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return f"{self.name} {self.surname} - {self.car}"