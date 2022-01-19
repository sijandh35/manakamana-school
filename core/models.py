from django.db import models
from tinymce.models import HTMLField

# Create your models here.
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

