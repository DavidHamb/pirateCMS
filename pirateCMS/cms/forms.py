from django import forms
from cms.models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'