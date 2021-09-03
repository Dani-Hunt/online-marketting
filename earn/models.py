from django.db import models


class Withdraw(models.Model):
    phone = models.CharField(max_length=11, null=False)
    amount = models.IntegerField(null=False)

