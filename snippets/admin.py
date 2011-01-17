from django.contrib import admin
from django.conf import settings

from snippets.models import *

class SnippetAdmin(admin.ModelAdmin):

        
    list_display = ('__unicode__', 'lang', 'active', 'date')
    list_filter = ('lang', 'categories') #, 'parent'

    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    if len(settings.LANGUAGES) < 2:
        exclude = ('lang',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user

        # always save model! this is where it is done
        obj.save()


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Category)

