from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
	"""Validar si el usuario tiene el perfil completo"""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_anonymous:
			if not request.user.is_staff:
				profile = request.user.profile
				if not profile.foto or not profile.biografia:
					if request.path not in [reverse('update_profile'), reverse('logout')]:
						return redirect('update_profile')

		response = self.get_response(request)
		return response
