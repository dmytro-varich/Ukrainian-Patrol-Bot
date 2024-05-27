import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
FILE_PATH = r'databases/ua_ru_words_homographs.txt'
API_KEY = os.getenv('API_KEY')

maintenance_mode = False


