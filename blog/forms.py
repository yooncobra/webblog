from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    is_agree = forms.BooleanField(label='약관동의',
            error_messages={'required': '약관에 동의해주셔야, 서비스 이용이가능합니다.'})

    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
