"""djangogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from noticias import views as views_noticias
from users import views as views_users

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('noticias', views_noticias.listar_noticias),
    # path('users/login', views_users.login),
    # path('users/registro', views_users.registro),
    path('', views_noticias.listar_posts, name='post'),
    path('noticias/new/', views_noticias.create_post, name='create_post'),
    path('users/login/', views_users.login_view, name='login'),
    path('users/logout/', views_users.logout_view, name='logout'),
    path('users/signup/', views_users.signup, name='signup'),
    path('users/me/profile/', views_users.update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
