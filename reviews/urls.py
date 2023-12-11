# reviews/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views

from .views import reviews, add_post, edit_post, delete_post, register, CustomLoginView

urlpatterns = [
    path('', reviews, name='reviews'),
    path('add_post/', add_post, name='add_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
