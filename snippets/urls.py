# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include

from snippets.models import Snippet

generic_options = {
    'queryset': Snippet.objects.all(),
    'template_name': 'snippets/snippet.html',
    'context_object_name': 'snippet',
}

# Generic views changed in Django 1.3, use new syntax if available
try:
    from django.views.generic.detail import DetailView
    detail_url = url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', DetailView.as_view(**generic_options), name='snippet')
except ImportError:
    from django.views.generic.list_detail import object_detail
    # convert from new attribute name to old one
    generic_options['template_object_name'] = generic_options.pop('context_object_name')
    detail_url = url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', object_detail, generic_options, name='snippet')


urlpatterns = patterns('',                       
    detail_url
)
    

