from django.urls import path
from .views import *

urlpatterns = [
    path( '', home, name='home'),
    path( 'work/', work, name='work'),
    path( 'work/error/', error, name='error'),
    path( 'work/noadmin/', noadmin, name='noadmin'),
]