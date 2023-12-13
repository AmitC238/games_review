# games_review/urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from reviews.views import add_post, edit_post, delete_post, register, CustomLoginView, CustomLogoutView, reviews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reviews, name='reviews'),
    path('add_post/', add_post, name='add_post'),
    path('edit/<post_id>/', edit_post, name='edit_post'),
    path('delete/<post_id>/', delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
