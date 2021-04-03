from django.urls import path

from . import views

app_name = "api.v1.services.email"

urlpatterns = [
    path('', views.SendView.as_view()),
]
