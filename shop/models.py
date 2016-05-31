from django.db import models
from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='shop_comment_set')  # or related_name='+'
    content = models.TextField()

# Create your models here.
