from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.domain"

router = routers.DefaultRouter()
router.register(r'', views.DomainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]