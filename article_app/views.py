from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from .forms import ArticleForm, CommentForm
from .models import Article, Comment, Category


def get_all_posts(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    data = {
        'posts': articles,
        'categories': categories,
        'username': auth.get_user(request).username
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
        'form': form,
        'username': auth.get_user(request).username
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
        'form': form,
        'username': auth.get_user(request).username
    }
    return render(request, 'add.html', context=data)


def main_page_view(request):
    data = {
        'username': auth.get_user(request).username
    }
    return render(request, 'main.html', context=data)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    elif request.method == 'GET':
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')