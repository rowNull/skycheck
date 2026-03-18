import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHERAPI_API_KEY")
API_URL = os.getenv("WEATHERAPI_URL")