from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/index.html', {'posts': posts})  # Render the index template with the posts context

def detail(request, slug):
    # post = Post.objects.get(slug=slug)  # Fetch the post with the given slug. This will crush the website if the slug does not exist
    post = get_object_or_404(Post, slug=slug)  # Fetch the post with the given slug or return a 404 error if not found
    return render(request, 'blog/detail.html', {'post': post})  # Render the detail template with the post context