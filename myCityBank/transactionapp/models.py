from email.policy import default
from enum import unique
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models
from myCityBank.transactionapp import Profile
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

account_type = [
    ("Savings", "Savings"),
    ("Current", "Current"),
    ("Fixed Deposit", "Fixed Deposit"),
]


#Create your models here.
class Account_table(models.Model):
    account_id = models.AutoField(primary_key =True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    account_balance = models.BigIntegerField(unique=False, null =True)
    account_type = models.CharField(choices=account_type, unique=False, max_length=20)
    account_number = models.CharField(unique=False, max_length=10, default=10101010)
    account_pin = models.IntegerField(default=0000, unique=False)


class Transaction_table(models.Model):
    transaction_id = models.AutoField(primary_key =True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    account = models.ForeignKey(Account_table, on_delete = models.CASCADE)
    transaction_type = models.CharField(unique=False, max_length=20)
    transaction_date = models.DateTimeField(default=timezone.now)
    account_number = models.CharField(unique=False, max_length = 10)
    transaction_amount = models.BigIntegerField(unique=False, null=True)
    recepent_number = models.CharField(unique=False, max_length=10, null=True)
    recepent_bank = models.CharField(unique=False, max_length=10, null=True)
    recepent_account = models.CharField(unique=False, max_length=10, null=True)




