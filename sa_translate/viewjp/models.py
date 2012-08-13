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
    textNumber = models.IntegerField(null=False)
    userID = models.IntegerField(default=0, null=False)
    Contents = models.TextField(null=False)
    transDate = models.DateTimeField(auto_now_add=True, auto_now=True)


    