from django.db import models

# Create your models here.

class Application(models.Model):
    nameOfEvent = models.CharField(max_length=99)
    socialMediaLinks = models.URLField()
    name = models.CharField(max_length=99)
    phoneNumber = models.CharField(max_length=99)
    email = models.EmailField()
    dateOfEvent = models.DateField()
    city = models.CharField(max_length=99)
    countOfClasses = models.IntegerField()
    countOfWinners = models.IntegerField()
    fileOfRules = models.FileField()
    deliveryAddress = models.CharField(max_length=99)
    comment = models.CharField(max_length=999)