from django.urls import path

from . import views

app_name = "api.v1.services.kyc"

urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
]