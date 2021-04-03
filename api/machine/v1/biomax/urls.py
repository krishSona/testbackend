from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.machine.v1.biomax"

router = routers.DefaultRouter()
router.register(r'attendance', views.AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]