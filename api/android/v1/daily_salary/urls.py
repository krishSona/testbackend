from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.android.v1.daily_salary"

router = routers.DefaultRouter()
router.register(r'workers', views.WorkerViewSet)
router.register(r'advances', views.AdvanceViewSet)

urlpatterns = [
    # path('session', views.session, name='session'),
    # path('worker', views.worker, name='worker'),
    path('transfer-to-bank', views.transfer_to_bank, name='transfer_to_bank'),
    path('', include(router.urls)),
]