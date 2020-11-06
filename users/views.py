from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .models import Profile


def register(request):
    if request.method == 'POST':
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')

    forms = UserRegisterForm()
    return render(request, 'users/register.html', {'forms': forms})


class Login(LoginView):
    template_name = 'users/login.html'


class Logout(LogoutView):
    template_name = 'users/logout.html'


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been updated !!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/profile.html', context)
