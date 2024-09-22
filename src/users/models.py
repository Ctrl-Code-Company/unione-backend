from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .managers import UserManager
from university.models import Major


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True)
    grade = models.IntegerField(
        validators=[
            MaxValueValidator(11),
            MinValueValidator(5)
        ],
        blank=True,
        null=True
    )
    coin = models.IntegerField(default=200)
    hobby = models.CharField(max_length=255, default="math")
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default=193)

    IELTS_CHOICES = (
        ("5-5.5", "5-5.5"),
        ("6-6.5", "6-6.5"),
        ("7-7.5", "7-7.5"),
        ("8-8.5", "8-8.5"),
        ("9", "9"),
        ("No", "No"),
    )
    MATH_CHOICES = (
        ("Foundation", "Foundation"),
        ("High", "High"),
        ("SAT", "SAT"),
        ("No", "No"),
    )

    english_score = models.CharField(max_length=255, choices=IELTS_CHOICES, default="6-6.5")
    math_score = models.CharField(max_length=255, choices=MATH_CHOICES, default="SAT")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)
    payment = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def get_fullname(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        return self.email
