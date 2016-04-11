# -*- coding: utf-8 -*-
import config

def wiki(request):
	context = {
		'wiki_name': config.WIKI_NAME,
		'wiki_slogan': config.WIKI_SLOGAN,
	}

	return context