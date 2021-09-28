from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    full_name = forms.CharField(
        label='ФИО',
    )
    password = forms.CharField(
        label='Пароль',
    )
    password2 = forms.CharField(
        label='Повторите пароль',
    )
    course_num = forms.IntegerField(
        label='Курс',
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

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_course_num(self):
        cd = self.cleaned_data
        if cd['course_num'] not in [1, 2, 3, 4]:
            raise forms.ValidationError('Course num should be from 1 to 4')
        return cd['course_num']
