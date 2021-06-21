"""
ASGI config for matrixfrommonitors project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from main.routing import ws_urlpatterns
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matrixfrommonitors.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})

