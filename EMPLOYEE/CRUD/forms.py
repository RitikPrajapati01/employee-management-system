from django import forms
from .models import Employees
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'email', 'mobile', 'skill', 'city']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'skill':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'})
        }