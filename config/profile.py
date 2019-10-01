import os, json, requests, re
import config.env as env
from classes.Configuration import Configuration

def __get_remote_configuration(index_type):
    headers = {
        'Content-Type': 'application/json'
    }
    remote_config = requests.get('/'.join(['http:/', env.INDEX_USER+':'+env.INDEX_PASSWORD+'@'+env.INDEX_URL, env.INDEX_COLLECTION, index_type]), headers=headers)
    print(str(remote_config.json()))
    if remote_config.status_code == 200:
        return remote_config.json()['_source']
    else:
        return None

def get_profile_information(index_type: str):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../profiles/%s.json'%index_type)
    try:
        file = open(filename, 'r')
        config = json.load(file)
        return config
    except:
        print("Type is new, generating configuration file")
        remote_config =  dict(__get_remote_configuration(index_type))
        new_file = open(filename, 'w')
        print(remote_config)
        new_file.write(json.dumps(remote_config))

        return remote_config

def update_profile_information(index_type: str, new_information: dict):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../profiles/%s.json'%index_type)
    print("Updating information")
    new_file = open(filename, 'w')
    new_file.write(json.dumps(new_information))
    return Configuration(new_information)
