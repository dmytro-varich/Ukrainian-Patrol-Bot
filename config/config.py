import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
FILE_PATH = os.getenv('FILE_PATH')
API_KEY = os.getenv('API_KEY')

maintenance_mode = False

