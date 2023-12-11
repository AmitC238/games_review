from django.urls import path
from .views import reviews, add_post, edit_post, delete_post

urlpatterns = [
    path('', reviews, name='reviews'),  # Change 'reviews/' to ''
    path('add_post/', add_post, name='add_post'),  # Added '/' after 'add_post'
    path('edit/<int:post_id>/', edit_post, name='edit_post'),  # Added '/' after 'edit/<int:post_id>'
    path('delete/<int:post_id>/', delete_post, name='delete_post'),  # Added '/' after 'delete/<int:post_id>'
]