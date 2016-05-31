from django.db import models
from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()

# Create your models here.
