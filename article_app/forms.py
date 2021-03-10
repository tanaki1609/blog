from django.forms import ModelForm

from article_app.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = 'title text category'.split()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = 'text'.split()
