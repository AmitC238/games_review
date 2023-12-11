"""
URL configuration for games_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# games_review/urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from reviews.views import add_post, edit_post, delete_post, register, CustomLoginView, reviews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reviews, name='home'), 
    path('reviews/', include('reviews.urls')),
    path('add_post/', add_post, name='add_post'),
    path('edit/<post_id>/', edit_post, name='edit_post'),
    path('delete/<post_id>/', delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

