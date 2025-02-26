from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import os
import creds

SCOPES = creds.SCOPES
SERVICE_ACCOUNT_FILE = creds.SERVICE_ACCOUNT_FILE
PARENT_FOLDER_ID = creds.PARENT_FOLDER_ID

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def list_files_in_drive_directory():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    query = f"'{PARENT_FOLDER_ID}' in parents and trashed=false"
    
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get('files', [])

    return files

def ids_and_names(files):
    ids = []
    names = []
    flag = 1

    for i in files:
        for y in i.values():
            if flag % 2 == 1:
                ids.append(y)
                flag += 1
            else:
                names.append(y)
                flag += 1
    return ids, names

def download_files_from_directory():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    download_folder = os.path.join(os.getcwd(), "downloaded_files")

    ids, names = ids_and_names(list_files_in_drive_directory())

    for file_id, file_name in zip(ids, names):
        file_path = os.path.join(download_folder, file_name)
        request = service.files().get_media(fileId=file_id)
        with open(file_path, 'wb') as f:
            f.write(request.execute())

download_files_from_directory()
