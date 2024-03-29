# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, NoReverseMatch

from datetime import datetime

from snippets import settings


class Category(models.Model):

    title = models.SlugField(max_length=30)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        # define these explicit for translation
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class SnippetManager(models.Manager):
    def current(self, language_code=None):
        qs = self.get_query_set().filter(active = True).exclude(end_date__lt=datetime.now()).exclude(start_date__gt=datetime.now())
        if language_code: qs = qs.filter(lang=language_code)
        return qs


class Snippet(models.Model):

    objects = SnippetManager()

    def get_upload_path(self, filename):
        if self.slug:
            filename = '%s/%s' % (self.slug, filename)
        return 'uploads/snippets/' + filename

    lang = models.CharField(_('Language'), max_length=5, choices=settings.LANGUAGES, default=settings.DEFAULT_LANGUAGE)
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)

    content = models.TextField(blank=True)
    attachment = models.FileField(upload_to=get_upload_path, blank=True, null=True)

    categories = models.ManyToManyField(Category, blank=True)

    link = models.URLField(verify_exists=False, blank=True)

    date = models.DateTimeField(default=datetime.now)


    active = models.BooleanField(default=True)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    parent = models.ForeignKey('self', verbose_name=_('Parent Snippet'), null=True, blank=True)

    creator = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.title or self.content[:76] or '<Empty Snippet>'

    def get_absolute_url(self):
        return reverse('snippet', kwargs={'slug':self.slug})

    class Meta:
        ordering = ('date',)
        unique_together = ('slug','parent')
        # define these explicit for translation
        verbose_name = _('snippet')
        verbose_name_plural = _('snippets')


