# -*- coding: utf-8 -*-
from django.conf import settings

def wiki(request):
	context = {
		'wiki_name': settings.WIKI_NAME,
		'wiki_slogan': settings.WIKI_SLOGAN,

		'wiki_engine': "django-simple-wiki (v0.0.3)",
	}

	return context