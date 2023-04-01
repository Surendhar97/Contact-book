from django.db import models

class Yellowpages(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    City=models.CharField(max_length=20)
    ContactNumber=models.IntegerField()