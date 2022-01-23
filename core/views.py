from django.shortcuts import render
from .models import *
from django.db.models import When, BooleanField, Case, Value
import datetime

# Create your views here.
def headers():
    try:
        return HeadersFooters.objects.first()
    except:
        return None

def index(request):
    today = datetime.date.today()
    header_footers = headers()
    home_page = HomePage.objects.first()
    teachers = Teachers.objects.all()
    events = Events.objects.annotate(upcoming=Case(When(date__gte=today, then=Value(True)), default=False, output_field=BooleanField())).order_by('-date')[:3]
    context = {
        'headers_footers': header_footers,
        'home_active': 'active',
        'home_obj': home_page,
        'teachers': teachers,
        'events': events,
        'event_image': events[0],
    }
    return render(request, 'index.html', context)

def events(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'events_active': 'active',
    }
    return render(request, 'events.html', context)

def teachers(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'teachers_active': 'active',
    }
    return render(request, 'teachers.html', context)

def schedule(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'schedule_active': 'active',
    }
    return render(request, 'schedule.html', context)

def gallery(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'gallery_active': 'active',
    }
    return render(request, 'contacts.html', context)

def contacts(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'contacts_active': 'active',
    }
    return render(request, 'contacts.html', context)