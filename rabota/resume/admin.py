from django.contrib import admin
from resume.models import Resume


class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['position', 'name', 'age']
    search_fields = ['position', 'country', 'skills']


admin.site.register(Resume, ResumeModelAdmin)

