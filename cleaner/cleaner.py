from config.env import INDEX_BANNED_CONTENT,ILLEGAL_CHARACTERS,DOCUMENT_USER_FIELD,INDEX_BANNED_USERS,INDEX_FIELD,INDEX_KEYWORDS,INDEX_BANNED_USERS,INDEX_USER,INDEX_PASSWORD,INDEX_URL,INDEX_NAME,CLEAN_FIELDS, INDEX_COLLECTION
import requests
import re
from config.profile import get_profile_information
from classes.Configuration import Configuration


def is_valid_user(dirty_object: dict, config):
    if dirty_object.__contains__(DOCUMENT_USER_FIELD):
        banned_users = config[INDEX_BANNED_USERS]
        if banned_users.__contains__(dirty_object[DOCUMENT_USER_FIELD]):
                return dict({ "result": False, "reason": 'User Banned'})
        return dict({ "result": True, "reason": 'User is not banned'})
    else:
        return dict({ "result": False, "reason": 'Field in dirty wansn\'t found'})

def is_valid_content(dirty_object: dict, config):
    for field in dirty_object:
        if config.__contains__(INDEX_BANNED_CONTENT):
            for banned_content in config[INDEX_BANNED_CONTENT]: 
                lookup_content = re.search(config, banned_content)
                if lookup_content:
                    return dict({"result": False, "reason": "Banned content found"})
    return dict({"result": True, "reason": "Content is legit"})

def clean_objects(dirty_object:dict, configuration):
    print(dirty_object)
    clean_object = dirty_object
    for field in iter(CLEAN_FIELDS):
        print(field)
        if clean_object.__contains__(field):
            print("Old field")
            print(clean_object[field])
            clean_object[field] = re.sub('['+"".join(ILLEGAL_CHARACTERS)+']', ' ', dirty_object[field])
            print("New field")
            print(clean_object[field])
    return clean_object
        