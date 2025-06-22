from django.db import models

# Create your models here.

# Models for the posts
class Post(models.Model):
    # All the posts should have a title
    title = models.CharField(max_length=255)
    slug = models.SlugField() # This is for the title to appear in the URL
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the post is created

    def __str__(self):
        return self.title