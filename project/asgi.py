import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path
import app.routing 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()






application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    'websocket' : URLRouter(app.routing.ws_patterns)
        
    
})











# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application
# from django.urls import path

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# from app.consumers import EchoConsumer

# ws_patterns = [
#     path('test/', EchoConsumer.as_asgi())
# ]



# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     'websocket' : URLRouter(ws_patterns)
        
    
# })



























# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator

# from django.urls import path


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()


# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,
     

#     # WebSocket chat handler

   
# })


#ws://127.0.0.0:8000/ws/sc/















# import os

# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter,URLResolver,URLRouter
# import app.routing
# from app.consumers import *
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')




# application = get_asgi_application()


# application = ProtocolTypeRouter(
#     {'http': get_asgi_application(),
#     'websocket' : URLRouter(app.routing.websocket_urlpatterns),
    
#     }
# )
