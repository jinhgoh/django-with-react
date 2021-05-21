from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    img = models.ImageField(blank=True, null=True)
    upload = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class ImageTest(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name