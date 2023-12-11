# reviews/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404
from .models import Post

@login_required
def reviews(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'reviews/reviews.html', context)

@login_required
def add_post(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST.get('title')
        body = request.POST.get('body')

        Post.objects.create(author=author, title=title, body=body)
        return redirect('reviews')
    return render(request, 'reviews/add_post.html')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.author = request.user
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')
        post.save()
        return redirect('reviews')
    return render(request, 'reviews/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('reviews')

class CustomLoginView(LoginView):
    template_name = 'reviews/login.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})
