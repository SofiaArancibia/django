from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()  # Fetch all posts from the database
    return render(request, 'blog/index.html', {'posts': posts})  # Render the index template with the posts context

def detail(request, slug):
    # post = Post.objects.get(slug=slug)  # Fetch the post with the given slug. This will crush the website if the slug does not exist
    post = get_object_or_404(Post, slug=slug)  # Fetch the post with the given slug or return a 404 error if not found
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # Create a comment instance but don't save it to the database yet
            comment.post = post
            comment.save()  # Save the comment to the database
            return redirect('detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post,
                                                'form': form})  # Render the detail template with the post context