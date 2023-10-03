from django.db import models

# Create your models here.

class profile(models.Model):
    image = models.FileField(upload_to="profile_images/", blank=True)
    description = models.CharField (max_length=20, null=True)

class aboutme(models.Model):
    text = models.TextField(null=True)