from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address!")
        if not username:
            raise ValueError("User must have a username!")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=25)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return f'User {self.username}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Animal(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(max_length=250)
    description = models.TextField()
    photo = models.ImageField(default='static/default.jpg', upload_to="images/")

    def __str__(self):
        return f'Animal "{self.name}"'


class Procedure(models.Model):
    CHOICES = (
        ("Grooming", "Grooming"),
        ("Diagnostics", "Diagnostics"),
        ("Surgery", "Surgery"),
        ("Therapy", "Therapy"),
    )
    name = models.CharField(max_length=250, choices=CHOICES)
    animal_name = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    information = models.TextField()

    def __str__(self):
        return f'Procedure: "{self.name}"'
