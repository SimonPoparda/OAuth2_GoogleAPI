from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = r'G:\Moje\Programowanie\Projekty_Data\Python\OAuth2.0\OAuth2.0_with_Python\Application\service_account.json'
PARENT_FOLDER_ID = '1uBpha5Ckko9WpwNj_DLdrJPStovByTv8'

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': 'Jestem_Szymon',
        'parents': [PARENT_FOLDER_ID]
    }

    file_1 = service.files().create(
        body=file_metadata,
        media_body=file_path,
    ).execute()

upload_photo('G:\Moje\Programowanie\Projekty_Data\Python\OAuth2.0\OAuth2.0_with_Python\Application\cute_doggy.jfif')
