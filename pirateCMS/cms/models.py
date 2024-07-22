from django.db import models

class Case(models.Model):
    name = models.fields.CharField(max_length=250)
