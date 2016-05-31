from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from programming.utils import random_name_upload_to


def min_length_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하라고 !!!')


class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 11)
        super(PhoneField, self).__init__(*args, **kwargs)
        validator = RegexValidator(r'^01[016789]\d{7,8}$',
                message='휴대폰 번호를 입력해주세요.')
        self.validators.append(validator)


@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100,
            validators=[min_length_validator],
            help_text='포스팅 제목을 100자 이내로 써주세요.')
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to=random_name_upload_to)
    phone = PhoneField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()

    def __str__(self):
        return self.message


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name