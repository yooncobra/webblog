from django.conf import settings
from django.shortcuts import redirect, render
from accounts.forms import SignupForm, SignupForm2


def signup(request):
    if request.method == 'POST':
        form = SignupForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm2()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def profile(request):
    return render(request, 'accounts/profile.html')