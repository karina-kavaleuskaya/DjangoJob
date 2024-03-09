from django.contrib import admin
from job.models import Job


class JobModelAdmin(admin.ModelAdmin):
    list_display = ['position', 'company_name', 'salary']
    search_fields = ['position', 'salary', 'country']


admin.site.register(Job, JobModelAdmin)
