from django.urls import path
from .views import Home,TermsAndConditions,PrivacyPolicies

urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('terms-and-conditions', TermsAndConditions.as_view(), name='terms_and_conditions'),
	path('privacy-policies', PrivacyPolicies.as_view(), name='privacy_policies'),
]