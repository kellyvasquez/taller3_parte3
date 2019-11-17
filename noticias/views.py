""" Noticias Views """

# Importar Librerias Django
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from noticias.forms import PostForm

#Models
from noticias.models import Post
#Variable Global
"""noticias = [
	{
		'titulo': 'Politica 2019',
		'usuario': {
			'nombre': 'Alvaro Uribe Velez',
			'foto': 'https://picsum.photos/60/60/?image=1027',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=1036',
	},
	{
		'titulo': 'Universo 2020',
		'usuario': {
			'nombre': 'Nasa',
			'foto': 'https://picsum.photos/60/60/?image=1005',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=903',
	},
	{
		'titulo': 'Infraestructura 2020',
		'usuario': {
			'nombre': 'Charles Chaplin',
			'foto': 'https://picsum.photos/60/60/?image=883',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://picsum.photos/200/200/?image=1076',
	},
]"""

# Create your views here.

@login_required
def listar_posts(request):
	"""Listar noticias"""
	posts = Post.objects.all().order_by('-created')
	return render(request, 'noticias/noticias.html', {'posts' : posts})

#def listar_noticias_anterior(request):
#	contenido = []
#	for noticia in noticias:
#		contenido.append("""
#			<p><strong>{nombre}</strong></p>
#			<p><small>{usuario} - <i>{timestamp}</i></small></p>
#			<figure><img src="{imagen}" /></figure>
#		""".format(**noticia))
#	return HttpResponse('<br>'.join(contenido))

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('post')
	else:
		form = PostForm()

	return render(
		request=request,
		template_name = 'noticias/new.html',
		context = {
			'form': form,
			'user': request.user,
			'profile': request.user.profile
		}
	)