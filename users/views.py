from django.shortcuts import render

def login(request):
	return render(request, 'users/login.html')

def registro(request):
	return render(request, 'users/registro.html')

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from users.models import Profile
from users.forms import ProfileForm, SignupForm

from django.db.utils import IntegrityError

def login_view(request):
	if request.method == 'POST':
		#print('*' * 10)
		username = request.POST['username']
		password = request.POST['password']
		#print(username, ':', password)
		#print('*' * 10)
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('post')
		else:
			return render(request, 'users/login.html', {'error': 'Inválido usuario o contraseña'})
	return render(request, 'users/login.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('login')

def signup(request):
	"""if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']

		if password != password_confirmation:
			return render(request, 'users/signup.html', {'error' : 'Las contraseñas no coinciden'})
		try:
			usuario = User.objects.create_user(username=username, password=password)
		except IntegrityError:
			return render(request, 'users/signup.html', {'error' : 'El usuario ya existe'})

		usuario.first_name = request.POST['first_name']
		usuario.last_name = request.POST['last_name']
		usuario.email = request.POST['email']
		usuario.save()

		profile = Profile(user=usuario)
		profile.save()

		return redirect('login')

	return render(request, 'users/signup.html')"""
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = SignupForm()

	return render(
		request=request,
		template_name = 'users/registro.html',
		context = {
			'form' : form
			}
		)



@login_required
def update_profile(request):
	profile = request.user.profile

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.cleaned_data
			profile.website = data['website']
			profile.telefono = data['telefono']
			profile.biografia = data['biografia']
			profile.foto = data['foto']
			profile.save()

			return redirect('update_profile')

	else:
		form = ProfileForm()
	
	return render(
		request=request,
		template_name = 'users/update_profile.html',
		context = {
			'profile': profile,
			'user':	request.user,
			'form' : form
			}
		)

@login_required
def detail(request):
	return render(request, 'users/detail.html')