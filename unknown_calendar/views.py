import os
import datetime
from calendar import HTMLCalendar

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

from .models import CalendarEvent

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
google_credentials = None

class CalendarView(generic.ListView):

    model = CalendarEvent
    template_name = 'unknown_calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cal = HTMLCalendar().formatmonth(2021, 12)
        context['calendar'] = mark_safe(cal)

        return context


def calendar_events(request):
    if google_credentials:
        service = build('calendar', 'v3', credentials=google_credentials)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            events = 'No upcoming events found'

        context = {}
        context['events'] = events

        return render(request, 'unknown_calendar/calendar.html', context)


def google_authorize(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(os.path.abspath(os.path.join( 
      os.path.dirname(__file__), 'client_secret.json')), scopes=SCOPES)

    flow.redirect_uri = 'http://localhost:8000/oauth2callback'
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')
    request.session['state'] = state

    return HttpResponseRedirect(authorization_url)

def oauth2callback(request):
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    state = request.session['state']

    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        os.path.abspath(os.path.join( 
        os.path.dirname(__file__), 'client_secret.json')), scopes=SCOPES, state=state)
    flow.redirect_uri = 'http://localhost:8000/oauth2callback'

    # Use the authorization/code server's response to fetch the OAuth 2.0 tokens.
    code = request.GET.get('code')
    flow.fetch_token(code=code)

    # Store credentials in the session.
    # ACTION ITEM: In a production app, you likely want to save these
    #              credentials in a persistent database instead.
    global google_credentials
    google_credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(google_credentials)

    return HttpResponseRedirect('/events')

def clear_credentials(request):
    if 'credentials' in request.session:
        del request.session['credentials']
    return ('Credentials have been cleared.<br><br>')

def credentials_to_dict(credentials):
    return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}
