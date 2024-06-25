from django.db import models


# Create Model for sticky notes application.
class Post(models.Model):
    title = models.CharField(max_length=200)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title
