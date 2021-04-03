from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.bank"

router = routers.DefaultRouter()
router.register(r'', views.BankViewSet)

urlpatterns = [
    path('', include(router.urls)),
]