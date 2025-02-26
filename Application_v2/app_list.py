from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import creds

SCOPES = creds.SCOPES
SERVICE_ACCOUNT_FILE = creds.SERVICE_ACCOUNT_FILE
PARENT_FOLDER_ID = creds.PARENT_FOLDER_ID
file_ids = creds.file_ids
file_names = creds.file_names

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def list_files_in_drive_directory():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    query = f"'{PARENT_FOLDER_ID}' in parents and trashed=false"
    
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])

    for i in files:
        for x, y in i.items():
            print(f'{x}: {y}')

list_files_in_drive_directory()