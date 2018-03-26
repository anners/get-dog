# settings.py
from dotenv import load_dotenv, find_dotenv
from pathlib import Path  # python3 only
import os

load_dotenv(find_dotenv())

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
ANN_CELL = os.getenv('ANN_CELL')
CHRIS_CELL = os.getenv('CHRIS_CELL')
TWILIO = os.getenv('TWILIO')
