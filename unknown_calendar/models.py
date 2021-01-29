from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
