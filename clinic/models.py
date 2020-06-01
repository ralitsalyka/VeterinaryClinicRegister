from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)


class Animal(models.Model):
    animal_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    species = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'"{self.name}"'


class Procedure(models.Model):
    name = models.CharField(max_length=250)
    animal_name = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    information = models.TextField()

    def __str__(self):
        return f'"{self.name}"'
