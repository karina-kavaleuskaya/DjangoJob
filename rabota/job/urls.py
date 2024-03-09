from django.urls import path
from job import views


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job_list/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job'),
    path('create_job/', views.create_job, name='create_job'),
    path('edit_job/<int:job_id>/', views.edit, name='edit_job'),
    path('job_delete/<int:job_id>/', views.job_delete, name='job_delete'),
    path('send_resume/<int:job_id>/', views.send_resume, name='send_resume'),
]
