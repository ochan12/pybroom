from config.env import PORT, DESTINATION_AUTH, DESTINATION_URL, INDEX_FIELD
from cleaner import cleaner
import subprocess
from bottle import run, post, request, response, get, route
from config.profile import get_profile_information, update_profile_information
from classes.Configuration import Configuration
import json, requests

@get('/')
def hello():
		return "This is PyBroom \nPlease configure me and start posting information so I can clean!"

@post('/clean', method="POST")    
def process():
        print("New Object to clean!!")
        new_object =  request.json
        print(new_object)
        config: Configuration = get_profile_information(new_object[INDEX_FIELD])
        valid_user = cleaner.is_valid_user(new_object, config)
        if valid_user['result'] is True:
            valid_content = cleaner.is_valid_content(new_object, config)
            if valid_content['result'] is True:
                clean_object = cleaner.clean_objects(new_object, config)
                print(str(clean_object))
                headers = {
                    'Authorization': DESTINATION_AUTH,
                    'Content-Type': 'application/json'
                }
                req = requests.post(url=DESTINATION_URL, data=json.dumps(clean_object), headers=headers)
                print("Sent:"+str(new_object['id'])+" - Code: "+str(req.status_code))
            else:
                print(valid_content['reason'])
        else:
            print(valid_user['reason'])

@post('/updateProfile', method="POST")    
def process():
        print("Updating database!!")
        new_object =  request.json
        update_profile_information(new_object.type, new_object.data)
        


run(host='localhost', port=PORT, debug=False)