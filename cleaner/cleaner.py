import logging

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
import re

logger = logging.getLogger(__name__)


def is_valid_user(dirty_object: dict):
    logger.info("Checking User")
    if "author" in dirty_object and "banned_users" in dirty_object:
        logger.info("Checking if author is banned users")
        banned_users = dirty_object['banned_users']
        if dirty_object['author'] in banned_users:
            logger.error("User banned")
            return dict({"result": False, "reason": 'User Banned'})
        logger.info("User is not banned")
        return dict({"result": True, "reason": 'User is not banned'})
    else:
        return dict({"result": True, "reason": 'No author field or banned_users'})


def is_valid_content(dirty_object: dict):
    logger.info("Checking content")
    if "banned_words" in dirty_object:
        for bannedWord in dirty_object['banned_words']:
            lookup_content = re.search(bannedWord, dirty_object['content'])
            if lookup_content:
                logger.error("Content banned")
                return dict({"result": False, "reason": "Banned content found"})
    return dict({"result": True, "reason": "Content is legit"})


def delete_project_fields(dirty_object: dict):
    for field in [
        "twitterUsers",
        "facebookUsers",
        "instagramUsers",
        "youtubeUsers",
        "banned_users",
        "banned_words",
        "keywords",
        "project_name",
        "project_slug",
        "createdAt",
        "index",
        "tags",
        "from_date",
        "to_date"
    ]:
        if field in dirty_object:
            dirty_object.__delitem__(field)
    return dirty_object


def clean_objects(dirty_object: dict):
    clean_object = dirty_object
    for field in ['content', 'text', 'title']:
        if field in clean_object:
            logger.info("Old field")
            logger.info(clean_object[field])
            clean_object[field] = re.sub('["\n", "\t", "\'", "\""]', ' ', dirty_object[field])
            logger.info("New field")
            logger.info(clean_object[field])
    return clean_object
