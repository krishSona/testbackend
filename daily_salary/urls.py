"""daily_salary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Core API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('django.contrib.auth.urls')),
    path('workers/',include('workers.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('api/android/v1/', include('api.android.v1.daily_salary.urls')),
    path('api/firebase/cloud_messaging/v1/', include('api.firebase.cloud_messaging.v1.daily_salary.urls')),
    path('api/machine/v1/biomax/', include('api.machine.v1.biomax.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # new apis for instasalary
    path('api/v1/company/', include('api.v1.company.urls')),
    path('api/v1/department/', include('api.v1.department.urls')),
    path('api/v1/designation/', include('api.v1.designation.urls')),
    path('api/v1/city/', include('api.v1.city.urls')),
    path('api/v1/state/', include('api.v1.state.urls')),
    path('api/v1/industry/', include('api.v1.industry.urls')),
    path('api/v1/employee_range/', include('api.v1.employee_range.urls')),
    path('api/v1/employee/', include('api.v1.employee.urls')),
    path('api/v1/employer/', include('api.v1.employer.urls')),
    path('api/v1/services/', include('api.v1.services.urls')),
    path('api/v1/user/', include('api.v1.user.urls')),
    path('api/v1/authentication/', include('api.v1.authentication.urls')),
    path('api/v1/bank/', include('api.v1.bank.urls')),
    path('api/v1/ifs/', include('api.v1.ifs.urls')),
    path('api/v1/level/', include('api.v1.level.urls')),
    path('api/v1/attendance/', include('api.v1.attendance.urls')),
    path('api/v1/statement/', include('api.v1.statement.urls')),
    path('api/v1/booking/', include('api.v1.booking.urls')),
    path('api/v1/qr_code/', include('api.v1.qr_code.urls')),
    path('api/v1/fcm/device/', include('api.v1.fcm.device.urls')),
    path('api/v1/verifier/', include('api.v1.verifier.urls')),
    path('api/v1/services/repayment/', include('api.v1.services.repayment.urls')),
    path('api/v1/services/email/', include('api.v1.services.email.urls')),
    path('api/v1/services/pg/', include('api.v1.services.pg.urls')),
    path('api/v1/services/kyc/', include('api.v1.services.kyc.urls')),
    path('api/v1/domain/', include('api.v1.domain.urls')),
    path('api/v1/application/', include('api.v1.application.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
