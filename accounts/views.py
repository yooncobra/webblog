from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, get_backends, authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.forms import SignupForm, SignupForm2
from accounts.forms import send_signup_confirm_email


def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            user = form.save()

            # backend_cls = get_backends()[0].__class__
            # backend_path = backend_cls.__module__ + '.' + backend_cls.__name__
            # https://github.com/django/django/blob/1.9/django/contrib/auth/__init__.py#L81
            # user.backend = backend_path

            authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])

            auth_login(request, authenticated_user)

            messages.info(request, '환영합니다. ;)')
            return redirect(settings.LOGIN_REDIRECT_URL)

            # 회원가입 시에, 이메일 승인
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # send_signup_confirm_email(request, user)
            # return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm2()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def signup_confirm(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request, '이메일을 인증했습니다. 로그인해주세요. ;)')
        return redirect(settings.LOGIN_URL)
    else:
        messages.error(request, '잘못된 경로로 접근하셨습니다. :-(')
        return redirect(settings.LOGIN_URL)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')