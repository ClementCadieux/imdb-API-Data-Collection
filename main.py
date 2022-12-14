import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_link = os.environ.get("API_LINK")
api_key = os.environ.get("API_KEY")

# response is the array of movies
response = requests.get(f"{api_link}/top_rated?api_key={api_key}&language=en-US&page=1").json()["results"]


