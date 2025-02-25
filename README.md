# OAuth2.0 with Google API with Python
This project focuses on uploading a file on Google Drive using Google APIs and Python

-----------------------------------------------------------------------------------------
## Process
<< I've created an application on Google Cloud

![image](https://github.com/user-attachments/assets/35394cd7-a3c9-4efb-9c71-a72c3c7a60d7)
![image](https://github.com/user-attachments/assets/ada0112a-ab37-47ce-adeb-755e369f19f7)

<< I've added service account, as well as created an API key
![image](https://github.com/user-attachments/assets/554753e6-a3fa-4086-a567-bffb5424c296)
![image](https://github.com/user-attachments/assets/d2c8ca45-fb60-423e-bf1a-671cd0769084)
![image](https://github.com/user-attachments/assets/a7e1dad9-2a3f-4da3-9c09-02dcac32094a)
![image](https://github.com/user-attachments/assets/dd3773b4-245e-4496-b5d1-9b650ad0cc7f)

<< Created repo, installed required packages:
`pip install google-api-python-client`

<< Written the code:
```python
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
![image](https://github.com/user-attachments/assets/672d9210-91c4-468b-98f0-2b683d1538f1)



