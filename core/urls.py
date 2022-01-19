from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('events/', events, name='events'),
    path('teachers/', teachers, name='teachers'),
    path('schedule/', schedule, name='schedule'),
    path('gallery/', gallery, name='gallery'),
    path('contacts/', contacts, name='contacts'),
]