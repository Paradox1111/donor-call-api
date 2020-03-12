from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donors', default=5)
    botsteward = models.CharField(max_length=100, default="Gretchen Bond", blank=True)
    orgName = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=100, default="", blank=True)
    email = models.CharField(max_length=100, default="", blank=True)
    paymentnum = models.CharField(max_length=100, default="", blank=True)
    yeartotal = models.CharField(max_length=100, default="", blank=True)
    lastgift = models.CharField(max_length=100, default="", blank=True)
    lastgiftdate = models.CharField(max_length=100, default="", blank=True)
    nextlastgift = models.CharField(max_length=100, default="", blank=True)
    nextlastgiftdate = models.CharField(max_length=100, default="", blank=True)
    comments = models.CharField(max_length=100, default="", blank=True)
    def __str__(self):
        return f'{self.orgName} {self.lastname}'