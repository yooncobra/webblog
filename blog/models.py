from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, help_text='포스팅 제목을 100자 이내로 써 주세요.')
    content = models.TextField()
    photo = models.ImageField(blank=True, help_text='이미지를 첨부하세요.')
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

