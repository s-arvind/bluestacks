from datetime import datetime

import pymongo

from config import MONGODB_HOST, MONGODB_PORT

mongo_client = None


# Create mongo db connection
def get_mongo_client():
    global mongo_client
    if mongo_client is None:
        mongo_client = pymongo.MongoClient(MONGODB_HOST, int(MONGODB_PORT))
    return mongo_client.test


# Mongo object
class MongoClientObject:
    db = get_mongo_client()

    def insert(self, data):
        # add search time to sort the recent searches
        data['searched_time'] = datetime.now()
        self.db.searches.insert_one(data)

    def update(self, data):
        # update search time when same text searched again
        self.db.searches.update(data, {"$set": {"searched_time": datetime.now()}})

    def find(self, query):
        doc = self.db.searches.find_one(query)
        return doc

    def find_all(self, query):
        docs = self.db.searches.find(query).sort("searched_time", -1).limit(5)
        results = []
        for doc in docs:
            results.append({"text": doc['text'], 'links': [item['link'] for item in doc['results']]})
        return results
