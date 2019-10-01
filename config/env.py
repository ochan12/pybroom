import json
from pathlib import Path  # python3 only
env_path = Path('.') / 'env.json'

config_file = json.load(open(env_path, 'r'))

PORT= config_file['PORT']
DESTINATION_URL=config_file['DESTINATION_URL']
DESTINATION_AUTH=config_file['DESTINATION_AUTH']
INDEX_FIELD=config_file['INDEX_FIELD']
INDEX_KEYWORDS=config_file['INDEX_KEYWORDS']
INDEX_BANNED_USERS=config_file['INDEX_BANNED_USERS']
INDEX_USER=config_file['INDEX_USER']
INDEX_PASSWORD=config_file['INDEX_PASSWORD']
INDEX_COLLECTION=config_file['INDEX_COLLECTION']
INDEX_URL=config_file['INDEX_URL']
INDEX_NAME=config_file['INDEX_NAME']
ILLEGAL_CHARACTERS=config_file['ILLEGAL_CHARACTERS']
DOCUMENT_USER_FIELD=config_file['DOCUMENT_USER_FIELD']
CLEAN_FIELDS=config_file['CLEAN_FIELDS']
INDEX_BANNED_CONTENT=config_file['INDEX_BANNED_CONTENT']