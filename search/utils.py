from googleapiclient.discovery import build
from config import GOOGLE_API_KEY, CX

google_client = None


# connect to google custom search engine
def get_google_client():
    global google_client
    if google_client is None:
        google_client = build("customsearch", 'v1', developerKey=GOOGLE_API_KEY).cse()
    return google_client


def get_search_results(text):
    google_client = get_google_client()
    search_results = []
    try:
        results = google_client.list(q=text, cx=CX).execute()
        for result in results['items'][:5]:
            search_results.append({"title": result['title'], "link": result['link']})
    except Exception as E:
        return {"error": "Something went wrong.", "details": str(E)}
    return search_results
