import requests
import re

def is_valid_user(dirty_object: dict):
    if dirty_object.__contains__('author'):
        banned_users = dirty_object['banned_users']
        if banned_users.__contains__(dirty_object['author']):
                return dict({ "result": False, "reason": 'User Banned'})
        return dict({ "result": True, "reason": 'User is not banned'})
    else:
        return dict({ "result": False, "reason": 'Field in dirty object wansn\'t found'})

def is_valid_content(dirty_object: dict):
    for bannedWord in dirty_object['banned_words']:
        lookup_content = re.search(bannedWord,dirty_object['content'])
        if lookup_content:
            return dict({"result": False, "reason": "Banned content found"})
    return dict({"result": True, "reason": "Content is legit"})

def clean_objects(dirty_object:dict):
    clean_object = dirty_object
    for field in ['content', 'text', 'title']:
        if clean_object.__contains__(field):
            print("Old field")
            print(clean_object[field])
            clean_object[field] = re.sub('["\n", "\t", "\'", "\""]', ' ', dirty_object[field])
            print("New field")
            print(clean_object[field])
    return clean_object
        