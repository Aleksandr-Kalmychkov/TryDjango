from django.db import models
# from .formatChecker import ContentTypeRestrictedFileField
from .validators import validate_file_size
from django.core.validators import FileExtensionValidator

# Create your models here.

class Application(models.Model):
    nameOfEvent = models.CharField(max_length=99)
    socialMediaLinks = models.URLField()
    name = models.CharField(max_length=99)
    phoneNumber = models.CharField(max_length=99)
    email = models.EmailField(null=True)
    dateOfEvent = models.DateField(null=True)
    city = models.CharField(max_length=99, null=True)
    countOfClasses = models.IntegerField(null=True)
    countOfWinners = models.IntegerField(null=True)
    fileOfRules = models.FileField(upload_to="media/", null=True, blank=True, validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'jpg', 'jpeg', 'png'])])
    deliveryAddress = models.CharField(max_length=99, null=True)
    comment = models.CharField(max_length=999, null=True)