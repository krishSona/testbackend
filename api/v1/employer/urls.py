from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.employer"

router = routers.DefaultRouter()
router.register(r'', views.EmployerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]