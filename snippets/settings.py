from django.conf import settings


LANGUAGES = getattr(settings, 'SNIPPETS_LANGUAGES', settings.LANGUAGES)

USE_I18N = settings.USE_I18N and len(LANGUAGES) > 1

DEFAULT_LANGUAGE = USE_I18N and LANGUAGES[0][0] or settings.LANGUAGE_CODE
