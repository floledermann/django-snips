from django.contrib import admin

from snippets import settings
from snippets.models import *

class SnippetAdmin(admin.ModelAdmin):
        
    if settings.USE_I18N:
        list_filter = ('lang', 'categories') #, 'parent'
        list_display = ('__unicode__', 'lang', 'active', 'date')
    else:
        list_filter = ('categories',) #, 'parent'
        list_display = ('__unicode__', 'active', 'date')
        exclude = ('lang',)

    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    save_as = True

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user

        # always save model! this is where it is done
        obj.save()


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Category)

