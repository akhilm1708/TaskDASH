from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json
from google.auth.transport.requests import Request
from datetime import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_FILE = 'token.json'

def authenticate_google():
    """Authenticate and return the Google Calendar service."""
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
        
        # Save credentials for the next run
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

    # Ensure due_date is formatted correctly (should include time)
    try:
        # Assuming due_date is in "YYYY-MM-DD" format, you need to add a time (e.g., 12:00 PM)
        # Adding a default time for the task
        formatted_due_date = datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%dT12:00:00")

        # Define the event
        event = {
            'summary': title,
            'start': {'dateTime': formatted_due_date, 'timeZone': 'America/Los_Angeles'},
            'end': {'dateTime': formatted_due_date, 'timeZone': 'America/Los_Angeles'},
        }

        # Insert the event into the calendar
        service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event '{title}' added to Google Calendar.")

    except ValueError:
        print("Error: The due date format should be 'YYYY-MM-DD'.")
