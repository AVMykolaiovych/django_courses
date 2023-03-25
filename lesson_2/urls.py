from django.urls import path
from .views import main, bio


urlpatterns = [
    path('main/', main, name="main"),
    path('bio/', bio, name="bio"),
]
