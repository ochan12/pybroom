<img src="./broom.png" alt="Pybroom" width="200"/>

# Pybroom
Python app that receives objects and cleans it according to defined fields and characters.

# Installation
You can access it through clone:
```
git clone https://github.com/ochan12/pybroom.git
```
or through [Docker](https://hub.docker.com/r/mateord/pybroom)
```
docker pull mateord/pybroom
```

# Configuration
Currently PyBroom is configured to work with objects like this
```json
{
    "author": "SomebodyVeryFamous",
    "content": "Some deep but banned content",
    "banned_users":["SomebodyNotSoFamous"], 
    "banned_words":["deep"]
}
```

# Execution
PyBroom needs a couple of arguments work more securely.
```s
docker run -p incoming_port:PORT \
-e USER_AUTH=BasicUserAuthIncomingObject \
-e PASSWORD_AUTH=BasicPasswordAuthIncomingObject \
-e PORT=PORT \
-e DESTINATION_URL="https://WhereDoYouSendIt.com" \
-e DESTINATION_AUTH="Authorization value for it's header in outgoing request" \
--name pybroom mateord/pybroom
```

