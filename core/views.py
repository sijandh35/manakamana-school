from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import When, BooleanField, Case, Value
import datetime, math, random

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
        'grade_list': Schedule.objects.all().distinct('grade').values_list('grade', flat=True)
    }
    return render(request, 'index.html', context)

def events(request):
    today = datetime.date.today()
    header_footers = headers()
    events = Events.objects.annotate(upcoming=Case(When(date__gte=today, then=Value(True)), default=False, output_field=BooleanField())).order_by('-date')
    page_size = request.GET.get('page_size', 6)
    page_no = request.GET.get('page_no', 1)
    prev_page = int(page_no) - 1 if int(page_no) > 1 else None
    next_page = int(page_no) + 1 if int(page_no) < math.ceil(events.count() / int(page_size)) else None
    events = events[(int(page_no) - 1) * int(page_size):int(page_no) * int(page_size)]
    context = {
        'headers_footers': header_footers,
        'events_active': 'active',
        'events': events,
        'prev_page': prev_page,
        'next_page': next_page,
        'current_page': page_no,
    }
    print(context)
    return render(request, 'events.html', context)
    

def teachers(request):
    header_footers = headers()
    teachers = Teachers.objects.all()
    page_size = request.GET.get('page_size', 8)
    page_no = request.GET.get('page_no', 1)
    prev_page = int(page_no) - 1 if int(page_no) > 1 else None
    next_page = int(page_no) + 1 if int(page_no) < math.ceil(teachers.count() / int(page_size)) else None
    teachers = teachers[(int(page_no) - 1) * int(page_size):int(page_no) * int(page_size)]
    context = {
        'headers_footers': header_footers,
        'teachers_active': 'active',
        'teachers': teachers,
        'prev_page': prev_page,
        'next_page': next_page,
        'current_page': page_no,
    }
    return render(request, 'teachers.html', context)

def schedule(request):
    grade = request.GET.get('grade', '1') 
    search = request.GET.get('search', None)
    if search:
        grade = search.split()[1] if len(search.split()) > 1 else search.split()[0]
    header_footers = headers()
    schedule = Schedule.objects.filter(grade=grade)
    color_list = ['background: linear-gradient(180deg, #fdc830, #f37335);', 'background: linear-gradient(180deg, #59fd30, #35b7f3);',
		'background: linear-gradient(180deg, #d35858, #f6e271);',
		'background: linear-gradient(180deg, #defd30, #9d35f3);',
		'background: linear-gradient(180deg, #94855d, #82b3ae);',
		'background: linear-gradient(180deg, #d604cc, #ff8f58);',
		'background: linear-gradient(180deg, #00ac81, #ff0479);',
		'background: linear-gradient(180deg, #8c9508, #722600);',
		'background: linear-gradient(180deg, #328399, #6d0051);',
		'background: linear-gradient(180deg, #8f8468, #cfff98);']
    schedule_data = [
        {
            'day': day,
            'periods': [{'subject_name': x.subject, 'period_time': x.period.time, 'note': x.note, 'color':random.choice(color_list)} for x in schedule.filter(day=day).distinct('period__id').order_by('period__id')]
        }for day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']]
    # print(schedule_data)
    grade_list = Schedule.objects.all().distinct('grade').values_list('grade', flat=True)
    context = {
        'headers_footers': header_footers,
        'schedule_active': 'active',
        'schedule': schedule_data,
        'grade_list': grade_list,
        'current_grade': grade,
    }

    return render(request, 'schedule.html', context)

def gallery(request):
    header_footers = headers()
    context = {
        'headers_footers': header_footers,
        'gallery_active': 'active',
    }
    return render(request, 'gallery.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        if name and email:
            subject = request.POST.get('subject', 'N/A')
            message = request.POST.get('message', 'N/A')
            Message.objects.create(name=name, email=email, subject=subject, message=message, date=datetime.datetime.now())
            return HttpResponse('success')
        else:
            return HttpResponse('Please provid valid name and email')
        