import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))

def verifyAuth(auth):
    if auth != os.environ["STUDYMATE_AUTH"]:
        return False
    else:
        return True
