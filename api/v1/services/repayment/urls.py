from django.urls import path

from . import views

app_name = "api.v1.services.repayment"

urlpatterns = [
    path('register/', views.RegisterView.as_view())
]
