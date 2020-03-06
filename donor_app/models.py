from django.db import models

# Create your models here.
class Steward(models.Model):
    name = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

class Donor(models.Model):
    steward = models.ForeignKey(Steward, on_delete=models.CASCADE, related_name='donors')
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
        return self.orgName