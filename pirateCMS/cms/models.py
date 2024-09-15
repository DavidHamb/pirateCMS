from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator

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

    class TypeTarget(models.TextChoices):
        CAPTURE_THE_FLAG = 'Capture the flag'
        BUG_BOUNTY = 'Bug bounty'
        IN_THE_WILD = 'In the wild'
        NOT_DEFINED = 'Not defined'

    name = models.fields.CharField(max_length=250, null=True)
    webpage = models.fields.URLField(null=True, blank=True)
    address = models.fields.CharField(max_length=250, null=True)
    description = models.fields.CharField(max_length=1000, null=True, blank=True)
    state = models.fields.CharField(choices=State.choices, max_length=20, default="Enumeration")
    OS = models.fields.CharField(choices=OperatingSystem.choices, max_length=10, default="Unknown")
    last_update = models.fields.DateField(null=True, default=date.today())
    type_of_target = models.fields.CharField(choices=TypeTarget.choices, max_length=20, default='Not defined')

    def __str__(self):
        return f'{self.name}'

class Methodology(models.Model):
    related_port = models.fields.IntegerField(null=True, validators=[MaxValueValidator(65535)])
    name = models.fields.CharField(max_length=250, null=True, blank=True)
    description = models.fields.CharField(max_length=20000, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Service(models.Model):
    name = models.fields.CharField(max_length=250, null=True)
    port = models.fields.IntegerField(null=False, default=0, validators=[MaxValueValidator(65535)])
    version = models.fields.CharField(max_length=10, null=True, blank=True)
    checked = models.fields.BooleanField(default=False)
    vulnerable = models.fields.BooleanField(default=False)
    linked_methodology = models.ForeignKey(Methodology, null=True, on_delete=models.SET_NULL)
    linked_case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'
    
class Note(models.Model):
    title = models.fields.CharField(max_length=50, null=True)
    text = models.fields.CharField(max_length=300, null=True)
    date = models.fields.DateField(null=False, default=date.today())
    linked_case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'
    
class Ressource(models.Model):
    title = models.fields.CharField(max_length=50, null=True)
    url = models.fields.URLField(null=True)
    linked_methodology = models.ForeignKey(Methodology, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
    
class Privesc(models.Model):
    os = models.fields.CharField(max_length=7, null=True)
    text = models.fields.CharField(max_length=20000, null=True)

    def __str__(self):
        return f'{self.os}'


