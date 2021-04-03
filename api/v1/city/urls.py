from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.city"

router = routers.DefaultRouter()
router.register(r'', views.CityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]