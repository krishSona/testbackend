from django.urls import path, include
from rest_framework import routers

from . import views

app_name = "api.v1.employee"

router = routers.DefaultRouter()
router.register(r'', views.EmployeeViewSet)

urlpatterns = [
    path('status/', views.EmployeeStatusView.as_view()),
    path('upload/', views.EmployeeBulkCreateView.as_view()),
    path('<uuid:rid>/', views.EmployeeViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('', include(router.urls)),
]
