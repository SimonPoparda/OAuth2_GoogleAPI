# OAuth2.0 with Google API with Python
This project focuses on uploading a file on Google Drive using Google APIs and Python

-----------------------------------------------------------------------------------------
## Process
<< I've created an application on Google Cloud

![image](https://github.com/user-attachments/assets/4ed2451e-cebc-4bc4-96fd-bade96a048ee)
![image](https://github.com/user-attachments/assets/a7160ad6-7968-4baf-8abb-de78ed1c58da)

<< I've added service account, as well as created an API key
![image](https://github.com/user-attachments/assets/1096283f-dab1-4cb7-9f31-cd61e0a01dff)
![image](https://github.com/user-attachments/assets/14a5d989-5ea8-4324-a48e-1d94e24e6f52)
![image](https://github.com/user-attachments/assets/07e1cc94-f196-4409-ac71-d6b30db192db)
![image](https://github.com/user-attachments/assets/6e125472-007c-4a6b-98b8-c6daee5411fd)

<< Created repo, installed required packages:
`pip install google-api-python-client`

<< Written the code:
```
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

upload_photo('Blue_Nature.jpg')
```

< Error: Service account info was not in the expected format, missing fields token_uri, client_email. 
Resulted from not creating service account and API key properly

<< Result:

![image](https://github.com/user-attachments/assets/39aed8e3-4b29-41ad-a394-67e7c7033a06)

