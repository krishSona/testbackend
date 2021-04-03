from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.employee_range"

router = routers.DefaultRouter()
router.register(r'', views.EmployeeRangeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]