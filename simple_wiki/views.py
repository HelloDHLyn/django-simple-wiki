# -*- coding: utf-8 -*-

import random

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView, ListView
from django.template import RequestContext
from django.http import HttpResponseRedirect

from .models import Article, ModifyHistory

class WikiHome(ListView):
    model = Article
    template_name = 'home.html'

class WikiContent(DetailView):
    model = Article
    template_name = 'article.html'

@login_required(login_url='/accounts/login/')
def modify_article(request, pk):
    try:
        article = Article.objects.get(title=pk)
    except ObjectDoesNotExist:
        content = ''
        code = ''
    else:
        content = article.content
        code = article.code

        if code == 403:
            raise PermissionDenied

    return render_to_response('modify.html', {'title': pk, 'content': content, 'code': code}, context_instance=RequestContext(request))

def find_article(request, pk):
    try:
        article = Article.objects.get(title__iexact=pk)
    except ObjectDoesNotExist:
        recommends = Article.objects.filter(title__contains=pk)
        context = {
            'title': pk,
            'recommends': recommends,
        }

        return render_to_response('notfound.html', context, context_instance=RequestContext(request))
    else:
        if article.code == 303:
            article = Article.objects.get(title=article.content)
            return render_to_response('article.html', {'article': article, 'redirect_origin': pk}, context_instance=RequestContext(request))
        else:
            return render_to_response('article.html', {'article': article}, context_instance=RequestContext(request))

def show_random(request):
    random_idx = random.randint(0, Article.objects.count() - 1)
    random_obj = Article.objects.all()[random_idx]
    return HttpResponseRedirect(reverse('wiki-article', kwargs={'pk': random_obj.title}))

def show_history_all(request):
    template_name = 'history.html'
    paged_template_name = 'history_paged.html'

    context = {
        'object_list': ModifyHistory.objects.all().order_by('-timestamp'),
        'page_template': paged_template_name,
        'is_global_history': True,
    }

    if request.is_ajax():
        template_name = paged_template_name

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def show_history(request, pk):
    template_name = 'history.html'
    paged_template_name = 'history_paged.html'

    context = {
        'object_list': ModifyHistory.objects.filter(title=pk).order_by('-timestamp'),
        'title': pk,
        'page_template': paged_template_name,
    }

    if request.is_ajax():
        template_name = paged_template_name

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def show_history_detail(request, pk):
    obj = ModifyHistory.objects.filter(code=pk)
    diff = obj[0].diff.split('\n')
    return render_to_response('history_detail.html', {'title': obj[0].title, 'diff': diff}, context_instance=RequestContext(request))

def show_wikiinfo(request):
    article_count = Article.objects.count()
    modify_count = ModifyHistory.objects.count()

    context = {
        'article_count': article_count,
        'modify_count': modify_count,
    }

    return render(request, 'wikiinfo.html', context, context_instance=RequestContext(request))