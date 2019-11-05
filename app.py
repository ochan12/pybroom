from config.env import PORT, DESTINATION_AUTH, DESTINATION_URL
import os, base64
from functools import wraps
from cleaner import cleaner
from flask import Flask, request, jsonify, Response
import json, requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
		return "This is PyBroom \nPlease configure me and start posting information so I can clean!\n"

def check(authorization_header):
    username = os.getenv('USER_AUTH')
    password = os.getenv('PASSWORD_AUTH')
    encoded_uname_pass = authorization_header.split()[-1]
    encoded_local = base64.b64encode((username + ":" + password).encode('utf-8')).decode('utf-8')
    print(encoded_local)
    print(encoded_uname_pass)
    if encoded_uname_pass == encoded_local :
        return True

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and check(authorization_header):
            return f(*args, **kwargs)
        else:
            return "Authentication failed\n", 401
        return f(*args, **kwargs)
    return decorated  

def process_object(new_object):
    print("Process Object")
    valid_user = cleaner.is_valid_user(new_object)
    if valid_user['result'] is True:
        valid_content = cleaner.is_valid_content(new_object)
        if valid_content['result'] is True:
            clean_object = cleaner.clean_objects(new_object)
            clean_object = cleaner.delete_project_fields(clean_object)
            headers = {
                'Authorization': DESTINATION_AUTH,
                'Content-Type': 'application/json'
            }
            req = requests.post(url=DESTINATION_URL, data=json.dumps(clean_object), headers=headers)
            print("Sent:"+str(new_object)+" - Code: "+str(req.status_code))
            return req.text
        else:
            return dict({'reason': "Invalid content", 'success': False})
    else:
        return dict({'reason': "Invalid user", 'success': False})


@app.route('/clean', methods=["POST"])    
@login_required
def clean():
    print("New Object to clean!!")
    new_object =  request.json
    print(new_object)
    try:
        result = process_object(new_object) 
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'reason': e}), 500
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(port=PORT, host='0.0.0.0')
    