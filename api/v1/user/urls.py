from django.urls import path

from . import views

app_name = "api.v1.user"

urlpatterns = [
    path('check/', views.UserCheckView.as_view()),
]