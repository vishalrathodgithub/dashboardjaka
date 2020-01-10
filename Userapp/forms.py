from Userapp.models import UserReg
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=UserReg
        fields='__all__'