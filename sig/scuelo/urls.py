from django.urls import path
from scuelo.views import home

urlpatterns = [
    path('', home , name='home'),
    # Other URL patterns if any
]
