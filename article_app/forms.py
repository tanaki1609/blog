from django.forms import ModelForm

from article_app.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = 'title text category'.split()