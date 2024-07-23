from django.db import models

class Case(models.Model):

    class State(models.TextChoices):
        ENUMERATION = 'Enumeration'
        FOOTHOLD = 'Foothold'
        PRIVESC = 'Privilege escalation'
        ROOTED = 'Rooted'
    
    class OperatingSystem(models.TextChoices):
        UNKNOWN = 'Unknown'
        LINUX = 'Linux'
        WINDOWS = 'Windows'

    name = models.fields.CharField(max_length=250, null=True)
    webpage = models.fields.URLField(null=True, blank=True)
    address = models.fields.CharField(max_length=250, null=True)
    description = models.fields.CharField(max_length=1000, null=True, blank=True)
    state = models.fields.CharField(choices=State.choices, max_length=20, default="Enumeration")
    OS = models.fields.CharField(choices=OperatingSystem.choices, max_length=10, default="Unknown")
    last_update = models.fields.DateField(null=True)
