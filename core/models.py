from django.db import models
from tinymce.models import HTMLField

# Create your models here.
GRADE_CHOICE = [
    ('1', '1'),
    ('2(Section A)','2(Section A)'),
    ('2(Section B)','2(Section B)'),
    ('3(Section A)','3(Section A)'),
    ('3(Section B)','3(Section B)'),
    ('4(Section A)','4(Section A)'),
    ('4(Section B)','4(Section B)'),
    ('5(Section A)','5(Section A)'),
    ('5(Section B)','5(Section B)'),
    ('6(Section A)','6(Section A)'),
    ('6(Section B)','6(Section B)'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]

DAY_CHOICE = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')
]

class HeadersFooters(models.Model):
    logo = models.ImageField(upload_to='logo', blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    work_time = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    info = HTMLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    google_url = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

class HomePage(models.Model):
    first_row_desc = HTMLField(blank=True, null=True)
    first_row_image = models.ImageField(upload_to='home_page_first_row', blank=True, null=True)
    first_row_title = models.CharField(max_length=255, blank=True, null=True)
    second_row_desc = HTMLField(blank=True, null=True)
    second_row_top_title_one = HTMLField(max_length=255, blank=True, null=True)
    second_row_top_title_two = HTMLField(max_length=255, blank=True, null=True)
    second_row_top_title_three = HTMLField(max_length=255, blank=True, null=True)
    second_row_top_title_four = HTMLField(max_length=255, blank=True, null=True)
    second_row_image_one = models.ImageField(upload_to='home_page_second_row_top_image_one', blank=True, null=True)
    second_row_image_two = models.ImageField(upload_to='home_page_second_row_top_image_two', blank=True, null=True)
    second_row_image_three = models.ImageField(upload_to='home_page_second_row_top_image_three', blank=True, null=True)
    second_row_image_four = models.ImageField(upload_to='home_page_second_row_top_image_four', blank=True, null=True)
    second_row_image_five = models.ImageField(upload_to='home_page_second_row_top_image_five', blank=True, null=True)
    second_row_image_six = models.ImageField(upload_to='home_page_second_row_top_image_six', blank=True, null=True)
    second_row_image_seven = models.ImageField(upload_to='home_page_second_row_top_image_seven', blank=True, null=True)
    second_row_image_eight = models.ImageField(upload_to='home_page_second_row_top_image_eight', blank=True, null=True)
    second_row_image_nine = models.ImageField(upload_to='home_page_second_row_top_image_nine', blank=True, null=True)
    second_row_image_ten = models.ImageField(upload_to='home_page_second_row_top_image_ten', blank=True, null=True)
    third_row_desc = HTMLField(blank=True, null=True)
    forth_row_desc = HTMLField(blank=True, null=True)

class Events(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    short_info = HTMLField(blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='events', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    event_by = models.CharField(max_length=255, blank=True, null=True)
    event_by_image = models.ImageField(upload_to='events_by', blank=True, null=True)

    def __str__(self):
        return self.title

class Teachers(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teachers', blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    google_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    name = models.CharField(max_length=255)
    time = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    grade = models.CharField(max_length=255, choices=GRADE_CHOICE)
    day = models.CharField(max_length=255, choices=DAY_CHOICE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    color_choice_one = models.CharField(max_length=255, blank=True, null=True)
    color_choice_two = models.CharField(max_length=255, blank=True, null=True)

    # def __str__(self):
    #     return self.grade + ' - ' + self.day + ' - ' + self.period.name 

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = HTMLField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name