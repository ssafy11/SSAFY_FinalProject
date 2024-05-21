from django.db import models
from django.contrib.auth.models import AbstractUser
from deposits.models import DepositProducts, DepositOptions
from savings.models import SavingProducts, SavingOptions

# Create your models here.

# 사용자 모델 정의
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=10, default='unKnown')
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    wealth = models.IntegerField(default=0)
    period = models.IntegerField(default=0)
    deposit = models.ManyToManyField(DepositProducts, blank=True, related_name='deposit_joined')
    saving = models.ManyToManyField(SavingProducts, blank=True, related_name='saving_joined')
    deposit_options = models.ManyToManyField(DepositOptions, blank=True, related_name='user_deposit_options')
    saving_options = models.ManyToManyField(SavingOptions, blank=True, related_name='users_saving_options')