from django.urls import path

from . import views

app_name = "api.v1.services"

urlpatterns = [
    path('sms/otp/', views.SmsOtpView.as_view()),
    path('activation_email/', views.ActivationEmailView.as_view())
]
