# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from django.views.generic.list_detail import object_detail

#from snippets import views
from snippets.models import Snippet

generic_options = {
    'queryset': Snippet.objects.all(),
    'template_name': 'snippets/snippet.html',
    'template_object_name': 'snippet'
    #'extra_context' : {'book_list' : get_books} # callabel will be evaluated

}

urlpatterns = patterns('',                       
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$', object_detail, generic_options, name='snippet'),
)

