from datetime import datetime
from django.db import models

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.now)
    stop_time = models.DateTimeField(default=datetime.now)

class GoogleCredential(models.Model):
    token = models.TextField()
    refresh_token = models.TextField()
    token_uri = models.TextField()
    client_id = models.TextField()
    client_secret = models.TextField()
    scopes = models.TextField()
