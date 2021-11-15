from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=10)
    edept = models.CharField(max_length=10)
    esal = models.FloatField()
