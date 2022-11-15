from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True)


class User(AbstractUser):
    gender = models.PositiveSmallIntegerField(validators=[MaxValueValidator(2), ], null=True, )
    age = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100), ], null=True, )