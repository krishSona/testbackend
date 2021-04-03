from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api.v1.attendance"

router = DefaultRouter()
router.register(r'', views.AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls))
]