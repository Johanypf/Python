import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def home():
    return {"mensaje": "Servidor funcionando"}


@app.get('/contact',response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Test</title>
        </head>
        <body>
            <h1>Hola soy un Web HTML!</h1>
            <p> Test parr</p>
        </body>
    </html>
    """


@app.get("/json", response_class=RedirectResponse)
async def redirect_fastapi():
    return "https://fastapi.tiangolo.com"










def run():
    store.get_categories()


if __name__ == "__main__":
    run()
