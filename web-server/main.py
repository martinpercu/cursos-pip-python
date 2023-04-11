import store
from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4,5]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h2>
        'name': '4timp',
        'telephone': '645098833'
    </h2>
    <h3>Esto es un H3
    </h3>
    
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()