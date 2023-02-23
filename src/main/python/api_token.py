import datetime
import pickle
import os
from os.path import join
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


def create_service(client_secret_file, api_name, api_version, *scopes):
    client_secret_file = client_secret_file
    api_service_name = api_name
    api_version = api_version
    scopes = [scope for scope in scopes[0]]
    cred = None
    pickle_file = join(os.getenv('USERPROFILE'), 'gm3a-data', f'token_{api_service_name}_{api_version}.pickle')

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        # print(api_service_name, 'service created successfully')
        return service
    except Exception as e:
        # print('Unable to connect.')
        # print(e)
        return None
