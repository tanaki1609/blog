from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, Select, PasswordInput

from article_app.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = 'title text category'.split()

        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название поста'
                }
            ),
            'text': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Текст'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Категория'
                }
            ),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = 'text'.split()


class RegisterForm(forms.Form):
    username = forms.CharField(label='Enter username: ', min_length=4, max_length=100,
                               widget=TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'placeholder': 'username'
                                   }
                               ))
    password1 = forms.CharField(label='Enter a password: ',
                                widget=PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'password'
                                }))
    password2 = forms.CharField(label='Repeat your password: ',
                                widget=PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'password'
                                }))

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('Пользователь уже существует')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password2 != password1:
            raise ValidationError('Пароли не совпадают')
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            's@n.ru',
            self.cleaned_data['password1'],
        )
        user.save()
        return user
