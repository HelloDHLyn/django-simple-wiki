from django.conf.urls import url

from .views import *
from .models import *

urlpatterns = [
	url(r'^$', WikiHome.as_view(), name='wiki-main'),
	url(r'^random/$', show_random, name='wiki-random'),
	url(r'^history/$', show_history_all, name='wiki-history'),
	url(r'^history/(?P<pk>[\w|\W]+)/$', show_history_detail, name='wiki-historydetail'),
	url(r'^(?P<pk>[\w|\W]+)/modify/$', modify_article, name='wiki-modify'),
	url(r'^(?P<pk>[\w|\W]+)/history/$', show_history, name='wiki-articlehistory'),
	url(r'^(?P<pk>[\w|\W]+)/$', find_article, name='wiki-article'),

	url(r'^api/search/$', search, name='wikiapi-search'),
	url(r'^api/modify/$', modify, name='wikiapi-modify'),
]