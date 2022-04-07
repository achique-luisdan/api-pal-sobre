from django.db import models


class Expense(models.Model):
    date = models.DateField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True, default=0.0)
    description = models.TextField(null=True, blank=True)


class Goal(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    since_date = models.DateField(null=True, blank=True)
    until_date = models.DateField(null=True, blank=True)
    days = models.IntegerField(null=True, blank=True, default=0.0)