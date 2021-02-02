import datetime as dt
import calendar

from google.oauth2 import credentials
from googleapiclient.discovery import build

from .models import GoogleCredential

def get_googlecal_events(year, month):
    credentials = []
    firt_day, last_day = calendar.monthrange(year, month)
    service = build('calendar', 'v3', credentials=credentials)

    now = dt.datetime.utcnow().isoformat() + 'Z'
    last = (dt.datetime.utcnow() + dt.timedelta(days=27)).isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary',
                                            timeMin=now, timeMax = last,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
    return events_result.get('items', [])
