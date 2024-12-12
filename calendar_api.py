from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_FILE = 'token.json'

def authenticate_google():
    #creds used as token to identify json file to save into google calendar
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            creds_data = json.load(token)
            creds = InstalledAppFlow.from_client_config(
                creds_data, SCOPES).credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'w') as token:
            json.dump({
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            }, token)
    return build('calendar', 'v3', credentials=creds)

def add_task_to_calendar(title, due_date):
    service = authenticate_google()
    event = {
        'summary': title,
        'start': {'dateTime': due_date, 'timeZone': 'America/Los_Angeles'},
        'end': {'dateTime': due_date, 'timeZone': 'America/Los_Angeles'},
    }
    service.events().insert(calendarId='primary', body=event).execute()
