from django import forms
from django.forms import (
    TextInput,
    PasswordInput,
    EmailInput,
    NumberInput,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.ModelForm):
    full_name = forms.CharField(
        label='ФИО',
        widget=TextInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': 'Иванов Иван Иванович',
            },
        ),
    )
    password = forms.CharField(
        label='Пароль',
        widget=PasswordInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': 'Пароль',
            },
        ),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=PasswordInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': 'Повторите пароль',
            },
        ),
    )
    course_num = forms.IntegerField(
        label='Курс',
        widget=NumberInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': '2',
            },
        ),
    )

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
            'email',
            'course_num',
            'password',
            'password2',
        )
        widgets = {
            'username': TextInput(
                attrs={
                    'class': 'authorization__input',
                    'placeholder': 'Никнейм',
                },
            ),
            'email': EmailInput(
                attrs={
                    'class': 'authorization__input',
                    'placeholder': 'mail@gmail.com',
                },
            ),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_course_num(self):
        cd = self.cleaned_data
        if cd['course_num'] not in [1, 2, 3, 4]:
            raise forms.ValidationError(
                'Номер вашего курса должен быть от 1 до 4'
            )
        return cd['course_num']


class SignInForm(AuthenticationForm):

    username = forms.CharField(
        max_length=254,
        widget=TextInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': 'Никнейм',
            },
        ),
    )
    password = forms.CharField(
        label='Пароль',
        widget=PasswordInput(
            attrs={
                'class': 'authorization__input',
                'placeholder': 'Пароль',
            },
        ),
    )

    class Meta:
        fields = (
            'username',
            'password',
        )
