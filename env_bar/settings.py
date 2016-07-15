# coding: utf-8
from django.conf import settings


INSERT_BEFORE = getattr(settings, 'ENV_BAR_INSERT_BEFORE', '</body>')
ENVIRONMENT = getattr(settings, 'ENV_BAR_ENVIRONMENT', 'Development')
SHOW = getattr(settings, 'ENV_BAR_SHOW', True)
