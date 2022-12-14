import requests
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import credentials

load_dotenv()

api_link = os.environ.get("API_LINK")
api_key = os.environ.get("API_KEY")
db_key_path = os.environ.get("DB_KEY_PATH")

# response is the array of movies
response = requests.get(f"{api_link}/top_rated?api_key={api_key}&language=en-US&page=1").json()["results"]

# Drop everything we don't need
# Feed the array back with only needed info

cred = credentials.Certificate(f"{db_key_path}")
firebase_admin.initialize_app(cred)

