from django.urls import path
from resume import views


urlpatterns = [
    path('resume_list/', views.resume_list, name='resume_list'),
    path('resume/<int:resume_id>/', views.resume_detail, name='resume'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('edit_resume/<int:resume_id>/', views.edit, name='edit_resume'),
    path('resume_delete/<int:resume_id>/', views.resume_delete, name='resume_delete'),

]
