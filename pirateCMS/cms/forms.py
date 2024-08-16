from django import forms
from cms.models import Case, Service, Methodology

STYLE_PARAMETERS = 'width: 500px; padding: 10px 30px; font-size: 16px;'
PICKLIST_STYLE_PARAMETERS = 'width: 500px; padding: 10px 30px; font-size: 16px; background-color: #cceeff'

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'webpage', 'address', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'webpage': forms.URLInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Website',
                }),                
            'address': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Target (ex: 127.0.0.1)'
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description'
                })
        }

class CaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['name', 'webpage', 'type_of_target', 'address', 'state', 'OS', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'webpage': forms.URLInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Website',
                }),  
            'type_of_target': forms.Select(attrs={
                'class': "form-control", 
                'style': PICKLIST_STYLE_PARAMETERS,
                }),              
            'address': forms.TextInput(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Target (ex: 127.0.0.1)'
                }),
            'state': forms.Select(attrs={
                'class': "form-control", 
                'style': PICKLIST_STYLE_PARAMETERS,
                }),
            'OS': forms.Select(attrs={
                'class': "form-control", 
                'style': PICKLIST_STYLE_PARAMETERS,
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description'
                })
        }

class AddServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['port', 'name', 'version']
        widgets = {
            'port': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Port',
                }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'version': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Version',
                }),
        }

class UpdateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'version', 'checked', 'vulnerable']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                }),
            'version': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                }),
            'checked': forms.CheckboxInput(attrs={
                'class': "form-control",
                }),
            'vulnerable': forms.CheckboxInput(attrs={
                'class': "form-control",
                }),
        }

class MethodologyForm(forms.ModelForm):
    class Meta:
        model = Methodology
        fields = ['related_port', 'name', 'description']

        widgets = {
            'related_port': forms.NumberInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Related port',
                }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),                
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Please write a short summary and then all necessary steps to attack the target ...'
                })
        }

class MethodologyUpdateForm(forms.ModelForm):
    class Meta:
        model = Methodology
        fields = ['related_port', 'name', 'description']

        widgets = {
            'related_port': forms.NumberInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Port',
                }),
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': STYLE_PARAMETERS,
                'placeholder': 'Name',
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                'style': STYLE_PARAMETERS,
                'placeholder': 'Description'
                })
        }