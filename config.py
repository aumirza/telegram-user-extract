from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

import os

SOURCE_ID = os.environ['SOURCE_ID'] #channel id with -
INVITE_MESSAGE = os.environ['MESSAGE'] 
API_ID = os.environ['API_ID']
API_HASH = os.environ['API_HASH']
TARGET_ID = os.environ['TARGET_ID'] #channel id with -