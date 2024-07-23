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

    def __str__(self):
        return f'{self.name}'

class Methodology(models.Model):
    name = models.fields.CharField(max_length=250, null=True, blank=True)
    description = models.fields.CharField(max_length=2000, null=True, blank=True)
    cve = models.fields.CharField(max_length=20, null=True, blank=True)
    related_service = models.fields.CharField(max_length=250, null=True, blank=True)
    version = models.fields.CharField(max_length=10, null=True, blank=True)
    documents = models.fields.CharField(max_length=100, null=True, blank=True)
    urls = models.fields.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Service(models.Model):
    name = models.fields.CharField(max_length=250, null=True, blank=True)
    port = models.fields.CharField(max_length=10, null=True, blank=True)
    version = models.fields.CharField(max_length=10, null=True, blank=True)
    checked = models.fields.BooleanField(default=False)
    vulnerable = models.fields.BooleanField(default=False)
    address = models.fields.CharField(max_length=250, null=True, blank=True)
    methodology = models.ForeignKey(Methodology, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'

