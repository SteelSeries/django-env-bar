# coding: utf-8
from __future__ import absolute_import, unicode_literals

import re

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_text
from django.template import TemplateSyntaxError
from django.template.loader import render_to_string

from . import settings as eb_settings

_HTML_TYPES = ('text/html', 'application/xhtml+xml')


class EnvBarMiddleware(object):
    """
    Middleware to render environment bar on response.
    """

    def process_response(self, request, response):
        # Check to see if we should even show the env bar
        if not eb_settings.SHOW:
            return response

        # Check for responses where the bar can't be inserted.
        content_encoding = response.get('Content-Encoding', '')
        content_type = response.get('Content-Type', '').split(';')[0]
        if any((getattr(response, 'streaming', False), 'gzip' in content_encoding, content_type not in _HTML_TYPES)):
            return response

        # Insert the toolbar in the response.
        content = force_text(response.content, encoding=settings.DEFAULT_CHARSET)
        insert_before = eb_settings.INSERT_BEFORE
        pattern = re.escape(insert_before)
        bits = re.split(pattern, content, flags=re.IGNORECASE)
        if len(bits) > 1:
            bits[-2] += self.render_bar()

            response.content = insert_before.join(bits)
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)
        return response

    def render_bar(self):
        try:
            context = {'environment': eb_settings.ENVIRONMENT}
            return render_to_string('env_bar/bar.html', context)
        except TemplateSyntaxError:
            if not apps.is_installed('django.contrib.staticfiles'):
                raise ImproperlyConfigured(
                    "The env bar requires the staticfiles contrib app. "
                    "Add 'django.contrib.staticfiles' to INSTALLED_APPS and "
                    "define STATIC_URL in your settings.")
            else:
                raise
