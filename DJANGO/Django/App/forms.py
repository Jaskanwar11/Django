from django import forms
from .models import AppVariety

class AppVarietyForm(forms.From):
    app_variety = forms.ModelChoiceField(quaryset = AppVariety.opjects.all(), label = "Select App variety")
