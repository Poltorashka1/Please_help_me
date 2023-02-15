from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from ticket.models import Ticket
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.

def userprofile(request):
    """Для просмотра профиля"""
    user_info = get_object_or_404(CustomUser, username=request.user.username)
    tiket = Ticket.objects.filter(passenger=user_info)
    return render(request, 'account.html', {'user_info': user_info, 'tiket': tiket})


def user_login(request):
    """Views для входа пользователя"""
    if request.method == "POST":
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('users:user_profile')
    else:
        login_form = forms.UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


class UserLogoutView(View):
    """Выход из аккаунта"""

    def get(self, request):
        logout(request)
        return redirect('users:login')


def register(request):
    """Views для регистрации пользователя"""
    if request.method == 'POST':
        user_form = forms.UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.name = user_form.cleaned_data['username']
            new_user.save()
            return redirect('users:login')
    else:
        user_form = forms.UserRegisterForm()
    return render(request, template_name='register.html', context={'user_form': user_form})


def admin_user(request):
    """Отображение всех пользователей"""
    all_user = CustomUser.objects.all()
    return render(request, 'admin_user.html', {'all_user': all_user})


def delete_user(request, pk):
    """удаление пользователя"""
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return redirect('users:admin_user')


def admin_ticket(request):
    """Создание билетика"""
    if request.method == 'POST':
        tik_form = forms.AddTicket(request.POST)
        if tik_form.is_valid():
            tik_form.save()
            return redirect('users:admin')
    else:
        tik_form = forms.AddTicket()
    return render(request, 'admin_ticket.html', {"tik_form": tik_form})


def admin(request):
    """Кастомная админка"""
    return render(request, 'admin.html', {})
