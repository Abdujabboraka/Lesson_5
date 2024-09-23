from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    price = models.IntegerField()
    max_speed = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=100)
    birth_date = models.IntegerField()
    color = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.name} {self.breed}"

class Phone(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    specs = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.model}"


class Home(models.Model):
    type = models.CharField(max_length=255)
    rooms = models.IntegerField()
    general_color = models.CharField(max_length=255)
    gas = models.BooleanField()
    electricity = models.BooleanField()
    area = models.IntegerField()

    def __str__(self):
        return f"{self.type} {self.area}"