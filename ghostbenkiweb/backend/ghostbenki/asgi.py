"""
ASGI config for zone01web zone01web.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangozone01web.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zone01web.settings')

application = get_asgi_application()
