import json

from fastapi import APIRouter, Depends
from http import HTTPStatus
from schemas import SearchQuery
from starlette.responses import JSONResponse
from utils import get_search_results

from connections import MongoClientObject

router = APIRouter()
mongo_client = MongoClientObject()


# get search
@router.get('/search/')
def get_search(search: SearchQuery = Depends()):
    query = {}
    search.register(query)
    item = mongo_client.find(query)
    if item:
        mongo_client.update(query)
        return item['results']
    else:
        results = get_search_results(search.text)
        if isinstance(results, dict):
            return JSONResponse(results, HTTPStatus.INTERNAL_SERVER_ERROR)
        query["text"] = search.text
        query['results'] = results
        mongo_client.insert(query)
    return JSONResponse(results, HTTPStatus.OK)


# get recent search
@router.get('/recent/')
def get_recent_searches(search: SearchQuery = Depends()):
    query = {}
    if search.text:
        query["text"] = {"$regex": f'.*{search.text}.*'}
    items = mongo_client.find_all(query)
    return JSONResponse(items, HTTPStatus.OK)
