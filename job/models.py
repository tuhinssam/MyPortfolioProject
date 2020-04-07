from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    links = models.CharField(max_length=255, default='SOME STRING')
    header = models.CharField(max_length=255, default='sample header')