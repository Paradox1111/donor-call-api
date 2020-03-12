from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donors', default=5)
    botsteward = models.CharField(max_length=100, default="Gretchen Bond")
    orgName = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    paymentnum = models.CharField(max_length=100, default="")
    yeartotal = models.CharField(max_length=100, default="")
    lastgift = models.CharField(max_length=100, default="")
    lastgiftdate = models.CharField(max_length=100, default="")
    nextlastgift = models.CharField(max_length=100, default="")
    nextlastgiftdate = models.CharField(max_length=100, default="")
    comments = models.CharField(max_length=100, default="", blank=True)
    def __str__(self):
        return f'{self.orgName} {self.lastname}'