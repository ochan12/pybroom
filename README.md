# Pybroom
Python app that receives objects and cleans it according to defined fields and characters.

# Installation

# Configuration
This application was developed to fetch configuration data from a remote [ElasticSearch]() database, so the structure
of the database source was `https://INDEX_URL/INDEX_COLLECTION/value_of_INDEX_FIELD`
```
PORT=8080
DESTINATION_URL='WhereDoYouWantThis.ToBe.Sent'
DESTINATION_AUTH='DoINeedLogin SecretHash'
INDEX_URL='Where is my database?'
INDEX_COLLECTION='Which collection within the database?'
INDEX_FIELD='Should contain the name of the field where I can find the document'
INDEX_KEYWORDS='Field within the configuration document that defines the keywords'
INDEX_BANNED_USERS='Field within the configuration document that defines which users shouldn't pass this filter'
INDEX_USER='To access the database'
INDEX_PASSWORD='To access the database'
DOCUMENT_USER_FIELD='Who post this content'
CLEAN_FIELDS=['Which', 'fields', 'should', 'I', 'clean']
```


# Execution

