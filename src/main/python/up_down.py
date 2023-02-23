from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
from api_token import create_service
from datetime import datetime
from os.path import join
import os
import json


def init_service(CLIENT_SECRET_FILE):
    api_name = 'drive'
    api_version = 'v3'
    scopes = ['https://www.googleapis.com/auth/drive']

    return create_service(CLIENT_SECRET_FILE, api_name, api_version, scopes)


def upload_db(CLIENT_SECRET_FILE):
    service = init_service(CLIENT_SECRET_FILE)
    file_name = join(os.getenv('USERPROFILE'), 'gm3a-data', 'database.db')
    mime_type = 'application/vnd.sqlite3'  # application/x-sqlite3

    file_metadata = {
        'name': "latest.db",
    }

    media = MediaFileUpload(file_name, mimetype=mime_type)
    res = service.files().list().execute()
    if len(res.get('files')) == 0:
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        file_id = {"id": file['id']}
        write_json(file_id, CLIENT_SECRET_FILE)
    else:
        f = open(CLIENT_SECRET_FILE)
        data = json.load(f)
        service.files().update(
            fileId=data['file_id']['id'],
            media_body=media
        ).execute()
        f.close()


def download_db(CLIENT_SECRET_FILE):
    service = init_service(CLIENT_SECRET_FILE)
    f1 = open(CLIENT_SECRET_FILE)
    data = json.load(f1)
    file_id = data['file_id']['id']
    f1.close()
    req = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=req)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)
    with open(join(os.getenv('USERPROFILE'), 'gm3a-data', 'database.db'), 'wb') as f:
        f.write(fh.read())
        f.close()


def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data['file_id'] = new_data
        file.seek(0)
        json.dump(file_data, file, indent=4)
