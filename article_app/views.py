from django.shortcuts import render, redirect

# Create your views here.
from .forms import ArticleForm, CommentForm
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(text=request.POST.get('text'),
                                             article_id=id)
            comment.save()
    comments = Comment.objects.filter(article_id=id)
    form = CommentForm()
    data = {
        'post': article,
        'comments': comments,
        'form': form
    }
    return render(request, 'post.html',
                  context=data)


def add_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    form = ArticleForm()
    data = {
        'form': form
    }
    return render(request, 'add.html', context=data)