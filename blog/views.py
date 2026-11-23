from django.shortcuts import render
from .models import Article


def index(request):

    articles = Article.objects.filter(is_published=True).order_by('-created_at')

    return render(request, 'blog/index.html', {
        'articles': articles
    })