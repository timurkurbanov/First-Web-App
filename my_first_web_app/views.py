from django.http import HttpResponse
from django.shortcuts import render
from my_first_web_app.models import Article
from datetime import date


def home_page(request):
  return render(request, 'index.html', {
    'articles': Article.objects.filter(draft=False).order_by('published_date'),
    'date': date.today(),
    'name': 'Blog by Timur'
    })
