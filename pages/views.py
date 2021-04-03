from django.views.generic import TemplateView

class Home(TemplateView):
	template_name = 'home.html'

class TermsAndConditions(TemplateView):
	template_name = 'terms_and_conditions.html'

class PrivacyPolicies(TemplateView):
	template_name = 'privacy_policies.html'