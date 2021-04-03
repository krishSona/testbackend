from django.urls import path, include
from api.v1.verifier import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.VerifierViewSet)

urlpatterns = [
    path('', include(router.urls))
]
