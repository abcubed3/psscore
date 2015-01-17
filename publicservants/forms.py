from django import forms

from .models import PublicServant

class PublicServantForm(forms.ModelForm):
    class Meta:
        model= PublicServant
    #code
