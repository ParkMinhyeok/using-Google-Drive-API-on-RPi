from __future__ import print_function
import cv2
import os.path
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

###Link Google Drive###
def AccessGoogleDrive():
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None

        if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                        creds.refresh(Request())
                else:
                        flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
                        creds = flow.run_local_server(port=0)

                with open('token.json', 'w') as token:
                        token.write(creds.to_json())

        return creds

###MakeDirectory###
def MakeDirectory(creds, folderName):
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
                'name': folderName,
                'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = service.files().create(body=file_metadata, fields='id').execute()
        folderID = folder.get('id')
        print("Make Directory ID:", folderID)
        return folderID

###Upload###
def UploadImg(creds, folderID, fileName):
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
                'name': fileName,
                'parents': [folderID]
        }
        media = MediaFileUpload('Target.jpg', mimetype='image/jpg')

        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(F'File ID: {file.get("id")}')

###Download###
def DownloadImg():
        import io
        from googleapiclient.http import MediaIoBaseDownload

        file_id = '12AKMzbjceoM6fQhvsS1Uuz4PeNxh1MwR'
        request = service.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False

        while done is False:
                status, done = downloader.next_chunk()
                print(F'Download{int(status.progress() * 100)}.')

        with open('savefile.png', 'wb') as f:
                f.write(file.getvalue())

def CamCapture():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
                return 0
        return cap

def CurrentDT():
        now = datetime.datetime.now()
        DateTime = now.strftime("%Y%m%d_%H%M%S")
        return DateTime


creds = AccessGoogleDrive()
folderName = CurrentDT()
folderID = MakeDirectory(creds, folderName)

cap = CamCapture()
if cap == 0:
        print("Cloud't find or open Camera")
        exit()

interval = 10
img_index = 1


while True:
        ret, frame = cap.read()
        if not ret:
                print("Could't find or open frame")
                break

        cv2.imwrite('Target.jpg', frame)
        cv2.waitKey(1)

        img_name = f"{img_index:03d}.jpg"
        UploadImg(creds, folderID, img_name)
        print(f"Save image : {img_name}")
        cv2.waitKey(1)

        img_index +=1

        cv2.imshow('frame', frame)
        if cv2.waitKey(interval * 1000) & 0xFF == 27:
                break

cap.release()
cv2.destroyAllWindows()
