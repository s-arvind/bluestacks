from decouple import config

GOOGLE_API_KEY = config('API_KEY')
CX = config('SEARCH_ENGINE_ID')
MONGODB_HOST = config('MONGODB_HOST')
MONGODB_PORT = config('MONGODB_PORT')