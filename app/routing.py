from django.urls import path

from . import consumers


ws_patterns = [
    path('/test/', consumers.EchoConsumer.as_asgi()),
    path('/test/ac/', consumers.MySocket.as_asgi()),

    path('test/sajal/',consumers.SajalSocket.as_asgi()),


    path('test/sync/',consumers.Asynconnect.as_asgi()),


    ]
