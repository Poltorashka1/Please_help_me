from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from ticket.models import Ticket

CustomUser = get_user_model()


class UserLoginForm(forms.Form):
    """Форма для входа пользователя """
    username = forms.CharField(max_length=128, label="Имя")
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class UserRegisterForm(forms.ModelForm):
    """Форма для регистрации пользователя"""
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    email = forms.EmailField(label="Почта", max_length=200, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'surname', 'email', 'phone')

    def clean_password2(self):
        """Проверка второго пароля"""
        cd = self.cleaned_data
        if len(cd['password2']) < 8:
            raise ValidationError('Пароль должен быть длиннее 8 символов')
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class AddTicket(forms.ModelForm):
    """Форма для создания билетика"""

    class Meta:
        model = Ticket
        fields = ('departure_city', 'city_of_arrival', 'time_of_arrival', 'price')
