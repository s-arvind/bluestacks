from typing import Dict, Any

from fastapi import Query
from pydantic import BaseModel
import hashlib


# create request schema
class SearchQuery(BaseModel):
    text: str = Query(None, alias='q')

    def register(self, query: Dict[str, Any]):
        if self.text:
            # generate search hash id to store searches in db
            search_id = hashlib.sha256(self.text.encode())
            query['search_id'] = search_id.hexdigest()
