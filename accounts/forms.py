from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    is_agree = forms.BooleanField(label='약관동의',
        error_messages = {
            'required': '약관동의를 해주셔야 가입이 됩니다.',
        })

    class Meta(UserCreationForm.Meta):
        # fields = ['username', 'email']
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('중복된 이메일')
        return email


class SignupForm2(UserCreationForm):
    email = forms.EmailField()
    is_agree = forms.BooleanField(label='약관동의',
        error_messages = {
            'required': '약관동의를 해주셔야 가입이 됩니다.',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        if email:
            User = get_user_model()
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('중복된 이메일')
        return email

    def save(self, commit=True):
        user = super(SignupForm2, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('땡~!!!')
        return answer