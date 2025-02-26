from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import os
import creds

SCOPES = creds.SCOPES
SERVICE_ACCOUNT_FILE = creds.SERVICE_ACCOUNT_FILE
PARENT_FOLDER_ID = creds.PARENT_FOLDER_ID
file_ids = creds.file_ids
file_names = creds.file_names


def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def download_files_from_directory():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    request = service.files().get_media(fileId=file_ids[0])
    
    download_folder = os.path.join(os.getcwd(), "downloaded_files")
    file_path = os.path.join(download_folder, file_names[0])
    

    with open(file_path, 'wb') as f:
        f.write(request.execute())

download_files_from_directory()