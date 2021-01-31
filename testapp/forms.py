from django import forms

from testapp.models import Confirmation

class ConfirmationForm(forms.ModelForm):

    class Meta:
        model=Confirmation
        fields="__all__"
