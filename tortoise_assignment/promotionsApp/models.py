from email.policy import default
from random import choices, expovariate
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .benifit_types import *

# Promotion Data Model


class PlanInfo(models.Model):
    plan_id = models.AutoField(primary_key=True)
    planName = models.TextField(null=False)
    amountOptions = models.IntegerField()
    tenureOptions = models.TextField()
    benefitPercentage = models.IntegerField()
    benefitType = models.CharField(
        choices=benifit_types, default=VOUCHER, max_length=256),
    startedDate = models.DateTimeField(null=True),
    usersNumber = models.IntegerField(null=True),
    timePeriod = models.IntegerField(null=True)


# User Data Model


class UserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    planID = models.ForeignKey(PlanInfo, on_delete=models.CASCADE)
    selectedAmount = models.IntegerField(null=False)
    selectedTenure = models.TextField(null=False)
    startedDate = models.DateTimeField(null=True)
    depositedAmount = models.IntegerField(null=False)
