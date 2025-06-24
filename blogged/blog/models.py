from django.db import models

# Create your models here.

# Models for the posts
class Post(models.Model):
    # All the posts should have a title
    title = models.CharField(max_length=255)
    slug = models.SlugField() # This is for the title to appear in the URL
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the post is created

    class Meta:
        ordering = ("-created_at",)  # Order posts by creation date, newest first

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link comment to a post
    # on_delete=models.CASCADE means that if the post is deleted, all its comments will also be deleted
    name = models.CharField(max_length=255)  # Author of the comment
    content = models.TextField()  # Content of the comment
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the comment is created

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.name} - {self.post.title}'