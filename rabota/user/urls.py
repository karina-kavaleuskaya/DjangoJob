from django.urls import path
from user import views


urlpatterns = [
    path('signup/', views.register, name='signup'),
]