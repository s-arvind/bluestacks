- install python3 and pip

- go to project and install requirements

    `pip install -u requirements.txt`

- create `.env` file and add this parameters
    
        BOT_TOKEN={DISCORD BOT TOKEN}
        API_KEY={GOOGLE CUSTOM SEARCH API TOKEN}
        SEARCH_ENGINE_ID={GOOGLE SEARCH ENGINE ID}
        MONGODB_HOST=localhost
        MONGODB_PORT=27017
        SEARCH=http://localhost:8000
    
- run and bot and search services
    
    `python bot/app.py`
    
    `python search/main.py`
    