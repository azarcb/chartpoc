from django.db import models

class Chartdata(models.Model):
    year = models.IntegerField(max_length=200)
    value = models.IntegerField(max_length=200)
