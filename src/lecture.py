from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title='Little API')


@app.get('/lectures', response_class=HTMLResponse)
def read_lecture():
    return """
    <html>
        <head>
            <title>Meu ola mundo em API</title>
        </head>
        <body>
            <h1>Ola mundo</h1>
        </body>
    </html> """
