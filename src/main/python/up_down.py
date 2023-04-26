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
    # list all files in the images directory
    images_path = join(os.getenv('USERPROFILE'), 'gm3a-data', 'images')
    file_names = os.listdir(images_path)

    file_name = join(os.getenv('USERPROFILE'), 'gm3a-data', 'database.db')
    mime_type = 'application/vnd.sqlite3'  # application/x-sqlite3

    file_metadata = {
        'name': "database.db",
    }

    media = MediaFileUpload(file_name, mimetype=mime_type)
    res = service.files().list(q="mimeType='{0}'".format(mime_type), fields="files(name)").execute()
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

    folder_id = '1Vquro1JjN9aF0ujy8ufdRvS0Nk7x_sPG'
    drive_images = []
    items = retrieve_images(service, folder_id)

    for i in items:
        drive_images.append(i['name'])

    for file in file_names:
        if file not in drive_images:
            file_metadata = {
                'name': file,
                'parents': [folder_id]
            }
            media = MediaFileUpload('{0}/{1}'.format(images_path, file), mimetype='image/jpeg')
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()


def download_db(CLIENT_SECRET_FILE):
    service = init_service(CLIENT_SECRET_FILE)
    f1 = open(CLIENT_SECRET_FILE)
    data = json.load(f1)
    file_id = data['file_id']['id']
    download_path = join(os.getenv('USERPROFILE'), 'gm3a-data', 'database.db')
    f1.close()
    download(service, file_id, download_path)

    # list all files in the images directory
    images_path = join(os.getenv('USERPROFILE'), 'gm3a-data', 'images')
    file_names = os.listdir(images_path)

    folder_id = '1Vquro1JjN9aF0ujy8ufdRvS0Nk7x_sPG'
    items = retrieve_images(service, folder_id)

    # Download each JPEG file and save it to disk
    for item in items:
        file_id = item['id']
        file_name = item['name']
        download_path = join(os.getenv('USERPROFILE'), 'gm3a-data', 'images', file_name)
        if file_name not in file_names:
            download(service, file_id, download_path)


def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data['file_id'] = new_data
        file.seek(0)
        json.dump(file_data, file, indent=4)


def retrieve_images(service, folder_id):
    jpeg_query = "mimeType='{0}' and parents in '{1}' and trashed=false".format('image/jpeg', folder_id)
    results = service.files().list(q=jpeg_query, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    return items


def download(service, file_id, path):
    request = service.files().get_media(fileId=file_id)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=file, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    file.seek(0)
    with open(path, 'wb') as f:
        f.write(file.read())
        f.close()
