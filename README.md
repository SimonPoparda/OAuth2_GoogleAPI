# OAuth2.0 with Google API with Python
This project focuses on uploading, listing, as well as downloading files from Google Drive using Google APIs and Python

-----------------------------------------------------------------------------------------
## Process
<< I've created an application on Google Cloud

![1](https://github.com/user-attachments/assets/8babeb44-1c8c-4f7b-9fc2-011fe5d30892)

![2](https://github.com/user-attachments/assets/1263e060-409d-4666-83f9-ea47efa9ef47)


<< I've added service account, as well as created an API key

![3](https://github.com/user-attachments/assets/08b8e2d8-6f85-4783-8b28-4e08a36757d0)

![4](https://github.com/user-attachments/assets/d6e4a9d4-58e9-47d4-8bcc-66c575642811)

![5](https://github.com/user-attachments/assets/60120b07-84ed-4762-849e-54ce65464bd7)

![6](https://github.com/user-attachments/assets/8aea270a-dbc8-4ccb-84f9-79ef5b2b194f)

<< Created repo, installed required packages:
`pip install google-api-python-client`

<< Written the code:
(example of uploading the file)
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

<< Result:

![image](https://github.com/user-attachments/assets/672d9210-91c4-468b-98f0-2b683d1538f1)



