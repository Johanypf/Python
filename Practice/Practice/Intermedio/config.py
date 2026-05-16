from dotenv import load_dotenv
import os

BASE_URL = 'https://newsapi.org/v2/everything' 

load_dotenv()
API_KEY = os.getenv("API_KEY")
