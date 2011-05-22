from django.conf import settings

LANGUAGES = getattr(settings, 'SNIPPETS_LANGUAGES', settings.LANGUAGES)
