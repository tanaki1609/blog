from django.shortcuts import render, redirect

# Create your views here.
from .forms import ArticleForm
from .models import Article, Comment, Category


def get_all_posts(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    data = {
        'posts': articles,
        'categories': categories
    }
    return render(request, 'index.html', context=data)


def get_post(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article_id=id)
    data = {
        'post': article,
        'comments': comments,
    }
    return render(request, 'post.html',
                  context=data)
