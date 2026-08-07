from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root_run():
    return {'msg': 'Hello world'}
