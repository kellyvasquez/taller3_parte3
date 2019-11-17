from django import forms

from noticias.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('user', 'profile', 'titulo', 'foto')