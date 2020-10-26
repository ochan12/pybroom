import logging
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

from config.env import DESTINATION_AUTH, DESTINATION_URL
import os, base64
from functools import wraps
from cleaner import cleaner
from flask import Flask, request, jsonify, Response
import json, requests
from tasks import make_celery
app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL=os.getenv('CELERY_BROKER_URL')
)
celery = make_celery(app)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "This is PyBroom \nPlease configure me and start posting information so I can clean!\n"


def check(authorization_header):
    username = os.getenv('USER_AUTH')
    password = os.getenv('PASSWORD_AUTH')
    encoded_uname_pass = authorization_header.split()[-1]
    encoded_local = base64.b64encode((username + ":" + password).encode('utf-8')).decode('utf-8')
    if encoded_uname_pass == encoded_local:
        return True


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and check(authorization_header):
            return f(*args, **kwargs)
        else:
            return "Authentication failed\n", 401
    return decorated  


def process_object(new_object):
    logger.info("Process Object")
    valid_user = cleaner.is_valid_user(new_object)
    if valid_user['result'] is True:
        logger.info("Is valid user")
        valid_content = cleaner.is_valid_content(new_object)
        if valid_content['result'] is True:
            logger.info("Content is okey")
            clean_object = cleaner.clean_objects(new_object)
            clean_object = cleaner.delete_project_fields(clean_object)
            headers = {
                'Authorization': DESTINATION_AUTH,
                'Content-Type': 'application/json'
            }
            req = requests.post(url=DESTINATION_URL,
                                data=json.dumps(clean_object),
                                headers=headers,
                                verify=False)
            logger.info("Sent:"+str(new_object)+" - Code: "+str(req.status_code))
            return req.text
        else:
            logger.error("Invalid content")
            return dict({'reason': "Invalid content", 'success': False})
    else:
        logger.error("Invalid user")
        return dict({'reason': "Invalid user", 'success': False})


@app.route('/clean', methods=["POST"])    
@login_required
def clean():
    logger.info("New Object to clean!!")
    new_object = request.json
    try:
        clean_task.delay(new_object)
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'reason': e}), 500
    return jsonify({'success': True}), 200


@celery.task()
def clean_task(new_object):
    result = process_object(new_object)
    return 'Done'


if __name__ == "__main__":
    app.run(port=8888, host='0.0.0.0')
