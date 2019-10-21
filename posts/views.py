from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)

@login_required
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)

@login_required
def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('posts:detail', id)

    else:
        form = PostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'posts/form.html', context)

@login_required
@require_POST
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:index')
    