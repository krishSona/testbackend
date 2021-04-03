from django.urls import path

from . import views
from api.v1.authentication.views import (
    RefreshTokenView,
)
app_name = "api.v1.authentication"

urlpatterns = [
    path('token/', views.UserLoginView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view()),
]