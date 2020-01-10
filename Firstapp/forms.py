from .models import ITJobs,MECHJobs,CIVILJobs
from django import forms

class ITJobForms(forms.ModelForm):
    class Meta:
        model=ITJobs
        fields='__all__'


class MECHJobForms(forms.ModelForm):
    class Meta:
        model=MECHJobs
        fields='__all__'

class CIVILJobForms(forms.ModelForm):
    class Meta:
        model=CIVILJobs
        fields='__all__'
