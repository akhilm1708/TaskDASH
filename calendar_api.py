from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json
from google.auth.transport.requests import Request
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_FILE = 'tasks.json'  # This will store the token
CLIENT_SECRETS_FILE = 'client_secrets.json'  # This file contains the client secrets

def authenticate_google():
    """Authenticate and return the Google Calendar service."""
    creds = None

    # Check if we already have a token stored
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token:
            creds_data = json.load(token)
            creds = InstalledAppFlow.from_client_config(
                creds_data, SCOPES).credentials  # This is wrong, see explanation below.

    # If no valid credentials are available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use the client secrets file to authenticate the user
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)  # Use the client secrets file
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token_data = {
                'token': creds.token,
                'refresh_token': creds.refresh_token,
                'token_uri': creds.token_uri,
                'client_id': creds.client_id,
                'client_secret': creds.client_secret,
                'scopes': creds.scopes
            }
            json.dump(token_data, token)
    
    return build('calendar', 'v3', credentials=creds)


def add_task_to_calendar(title, due_date):
    """Add a task to the Google Calendar."""
    service = authenticate_google()

    try:
        # Check that the date format is correct
        formatted_due_date = datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%dT12:00:00")
        event = {
            'summary': title,
            'start': {'dateTime': formatted_due_date, 'timeZone': 'America/Los_Angeles'},
            'end': {'dateTime': formatted_due_date, 'timeZone': 'America/Los_Angeles'},
        }

        # Insert the event into the Google Calendar
        service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event '{title}' added to Google Calendar.")

    except ValueError:
        print("Error: The due date format should be 'YYYY-MM-DD'.")
