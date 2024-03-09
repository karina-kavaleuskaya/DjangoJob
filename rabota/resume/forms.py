from django import forms
from resume.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ("position", "name", 'age', 'personality', 'country', 'skills')