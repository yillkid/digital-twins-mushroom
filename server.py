import os
import json
import gspread
import pytz
import time
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from get_env import get_environment_params
from callback import set_device
from datetime import datetime

load_dotenv()

url_google_sheet = os.getenv("GOOGLE_SHEET_URL")
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret/key.json', scope)
client = gspread.authorize(creds)

while True:
    env_param = {"temperature":"","humidity":"", "drip":"", "fan":""}
    google_sheet = client.open_by_url(os.getenv("GOOGLE_SHEET_URL"))
    get_environment_params(google_sheet, env_param)
    set_device(google_sheet, env_param)
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')

    print(formatted_now + " : "  + json.dumps(env_param))
    time.sleep(5)
