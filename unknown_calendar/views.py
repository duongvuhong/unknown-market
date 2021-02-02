import os

from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
import google_auth_oauthlib.flow

from .models import CalendarEvent
from .calendar import Calendar

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
google_credentials = None

class CalendarView(generic.ListView):

    model = CalendarEvent
    template_name = 'unknown_calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cal = Calendar(2021, 2)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        return context


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

    # TODO: likely save these credentials in a persistent database instead.
    global google_credentials
    google_credentials = flow.credentials

    print({'token': google_credentials.token,
    'refresh_token': google_credentials.refresh_token,
    'token_uri': google_credentials.token_uri,
    'client_id': google_credentials.client_id,
    'client_secret': google_credentials.client_secret,
    'scopes': google_credentials.scopes})
    return HttpResponseRedirect('/')
