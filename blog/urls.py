# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from blog.models import Artigo

urlpatterns = patterns('',
    (r'artigos', 'django.views.generic.date_based.archive_index',
        {'queryset': Artigo.objects.all(),
            'date_field': 'publicacao'}),
    (r'^artigo/(?P<artigo_id>\d+)/$', 'blog.views.artigo'),
)

