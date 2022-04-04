from django.db import models


class Plant(models.Model):
    image = models.ImageField(default='defaultplant.svg', null=True, upload_to='plant_pics')
    commonname = models.CharField(max_length=50)
    cultivar = models.CharField(max_length=40, blank=True)
    species = models.CharField(max_length=40, blank=True)
    genus = models.CharField(max_length=40, blank=True)
    family = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=40, blank=True)
    mintemp = models.CharField(max_length=40, blank=True)
    maxtemp = models.CharField(max_length=40, blank=True)
    lightreq = models.CharField(max_length=40, blank=True)
    waterreq = models.CharField(max_length=5, blank=True)
    minzone = models.CharField(max_length=3, blank=True)
    maxzone = models.CharField(max_length=3, blank=True)