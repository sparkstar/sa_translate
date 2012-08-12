from django.db import models

# Create your models here.

class Text(models.Model):
    textNumber = models.IntegerField()
    textPos = models.IntegerField()
    textPtr = models.IntegerField()
    unknown1 = models.IntegerField()
    unknown2 = models.IntegerField()
    hexString = models.CharField(max_length=255)

class translateText(models.Model):
    transTextNumber = models.IntegerField()
    