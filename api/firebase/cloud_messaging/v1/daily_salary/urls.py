from django.urls import path
from . import views

app_name = "api.firebase.cloud_messaging.v1.daily_salary"

urlpatterns = [
    path('registration', views.registration, name='registration')
]