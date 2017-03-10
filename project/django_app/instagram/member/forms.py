from django import forms
from django.contrib.auth.password_validation import validate_password

from member.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=User.CHOICES_GENDER, widget=forms.RadioSelect())
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput)
    nickname = forms.CharField(max_length=30)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('username already exists')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        validate_password(password2)

        if password1 != password2:
            raise forms.ValidationError('password not equal')
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        password2 = self.cleaned_data['password2']
        email = self.cleaned_data['email']
        gender = self.cleaned_data['gender']
        nickname = self.cleaned_data['nickname']

        # if User.objects.filter(username=username).exists():
        #     form.add_error('username', 'username already exist')
        # if password1 != password2:
        #     form.add_error('password1', 'password1 and password2 not equal')
        # else:
        user = User.objects.create_user(
            username=username,
            password=password2
        )
        user.email = email
        user.gender = gender
        user.nickname = nickname
        user.save()
        return user
