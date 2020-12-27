import uvicorn
from fastapi import FastAPI

from routers import router

app = FastAPI(title='Google Search Service')
app.include_router(
    router,
    prefix='/api',
    tags=['Google Search'],
)


def main():
    uvicorn.run(app, host='127.0.0.1', port=8000)


if __name__ == '__main__':
    main()
