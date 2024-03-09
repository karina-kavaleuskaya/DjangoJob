from django.db import models
from django.conf import settings


class Job(models.Model):
    position = models.CharField(max_length=250)
    company_name = models.CharField(max_length=350)
    project_description = models.TextField()
    job_requirement = models.TextField()
    country = models.TextField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    salary = models.TextField(max_length=50)



