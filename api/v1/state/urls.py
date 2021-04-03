from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.state"

router = routers.DefaultRouter()
router.register(r'', views.StateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]