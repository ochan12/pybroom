import os
from dotenv import load_dotenv
try:
    load_dotenv()
except:
    pass
DESTINATION_URL=os.environ['DESTINATION_URL']
DESTINATION_AUTH=os.environ['DESTINATION_AUTH']

