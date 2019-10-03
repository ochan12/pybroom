import json, os
from pathlib import Path  # python3 only
from config.args import ARGS


if os.environ.__contains__('ENVIRONMENT') and os.environ['ENVIRONMENT'] == 'Production':
    PORT= os.environ['PORT']
    DESTINATION_URL=os.environ['DESTINATION_URL']
    DESTINATION_AUTH=os.environ['DESTINATION_AUTH']
    INDEX_FIELD=os.environ['INDEX_FIELD']
    INDEX_KEYWORDS=os.environ['INDEX_KEYWORDS']
    INDEX_BANNED_USERS=os.environ['INDEX_BANNED_USERS']
    INDEX_USER=os.environ['INDEX_USER']
    INDEX_PASSWORD=os.environ['INDEX_PASSWORD']
    INDEX_COLLECTION=os.environ['INDEX_COLLECTION']
    INDEX_URL=os.environ['INDEX_URL']
    INDEX_NAME=os.environ['INDEX_NAME']
    ILLEGAL_CHARACTERS=os.environ['ILLEGAL_CHARACTERS']
    DOCUMENT_USER_FIELD=os.environ['DOCUMENT_USER_FIELD']
    CLEAN_FIELDS=os.environ['CLEAN_FIELDS']
    INDEX_BANNED_CONTENT=os.environ['INDEX_BANNED_CONTENT']
elif ARGS.environment == 'Development':
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
