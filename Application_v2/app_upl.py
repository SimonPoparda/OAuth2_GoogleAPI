from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import creds

SCOPES = creds.SCOPES
SERVICE_ACCOUNT_FILE = creds.SERVICE_ACCOUNT_FILE
PARENT_FOLDER_ID = creds.PARENT_FOLDER_ID

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': file_path.split('/')[-1],
        'parents': [PARENT_FOLDER_ID]
    }

    file_1 = service.files().create(
        body=file_metadata,
        media_body=file_path,
    ).execute()

upload_photo(creds.picture_upload)


