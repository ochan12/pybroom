from config.env import PORT, DESTINATION_AUTH, DESTINATION_URL
from cleaner import cleaner
from multiprocessing import Pool
from flask import Flask, request, jsonify
from config.profile import get_profile_information, update_profile_information
from classes.Configuration import Configuration
import json, requests
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
		return "This is PyBroom \nPlease configure me and start posting information so I can clean!\n"

def process_object(new_object):
    valid_user = cleaner.is_valid_user(new_object)
    if valid_user['result'] is True:
        valid_content = cleaner.is_valid_content(new_object)
        if valid_content['result'] is True:
            clean_object = cleaner.clean_objects(new_object)
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


@app.route('/clean', methods=["POST"])    
def clean():
        print("New Object to clean!!")
        new_object =  request.json
        print(new_object)
        try:
            pool = Pool(processes=1)
            result = pool.apply_async(process_object,[new_object],callback=exit) 
        except Exception as e:
            return jsonify({'success': False, 'reason': e}), 500
        return jsonify({'success': True}), 200

if __name__ == "__main__":
    app.run(port=8888, host='0.0.0.0')
    