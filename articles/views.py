from django.shortcuts import render

from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'
    article = Article.objects.order_by('-published_at')

    context = {'object_list': article,
             }

    return render(request, template, context)
