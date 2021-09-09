from django.db import models
from django.core.validators import MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField




class Withdraw(models.Model):
    phone = models.CharField(max_length=11, null=False)
    amount = models.IntegerField(null=False)

class Quiz(models.Model):
    firstname = models.CharField(null=False, default='', max_length=10)
    lastname = models.CharField(null=False, default='', max_length=10)
    age = models.IntegerField(null=False)
    gender = models.CharField(null=False,max_length=6)
    phone = PhoneNumberField(unique = True, null = False, blank = False)
    id_number = models.PositiveIntegerField(null = False, primary_key=True, validators=[MaxValueValidator(8)])


class Quiz1(models.Model):
    location = models.CharField(null=False, default='', max_length=100)
    name = models.CharField(null=False, default='', max_length=100)
    like = models.CharField(null=False,max_length=6)
    rate = models.CharField(null=False, default='', max_length=100)
    dislike = models.CharField(null=False, default='', max_length=100)
    rules = models.CharField(null=False, default='', max_length=100)




