import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')
BASE_URL = os.getenv('BINANCE_BASE_URL')
RECV_WINDOW = int(os.getenv('RECV_WINDOW'))
