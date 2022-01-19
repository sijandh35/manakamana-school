from django.shortcuts import render
from .models import *

# Create your views here.
header_footers = HeadersFooters.objects.first()

def index(request):
    context = {
        'headers_footers': header_footers,
        'home_active': 'active',
    }
    return render(request, 'index.html', context)

def events(request):
    context = {
        'headers_footers': header_footers,
        'events_active': 'active',
    }
    return render(request, 'events.html', context)

def teachers(request):
    context = {
        'headers_footers': header_footers,
        'teachers_active': 'active',
    }
    return render(request, 'teachers.html', context)

def schedule(request):
    context = {
        'headers_footers': header_footers,
        'schedule_active': 'active',
    }
    return render(request, 'schedule.html', context)

def gallery(request):
    context = {
        'headers_footers': header_footers,
        'gallery_active': 'active',
    }
    return render(request, 'contacts.html', context)

def contacts(request):
    context = {
        'headers_footers': header_footers,
        'contacts_active': 'active',
    }
    return render(request, 'contacts.html', context)