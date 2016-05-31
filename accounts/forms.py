from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('땡~!!!')
        return answer