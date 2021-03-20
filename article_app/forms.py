from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, Select

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

