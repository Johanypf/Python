from dotenv import load_dotenv
import os


load_dotenv()

BASE_URL = 'https://newsapi.org/v2/everything' 


API_KEY = os.getenv("API_KEY")
OPEN_KEY = os.getenv("OPEN_API_KEY")

print(API_KEY)
print(OPEN_KEY)