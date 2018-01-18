# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Article

# Create your views here.

def first_view(request):

    articles = Article.objects.all
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)
