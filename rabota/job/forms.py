from django import forms
from job.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ("position", "company_name", 'project_description', 'job_requirement', 'country', 'salary')