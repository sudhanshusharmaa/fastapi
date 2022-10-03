from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return "How can I help you sir"

@app.get('/about')
def about():
    return {'data':'about page'}


@app.get('/blog/unpublished')
async def unpublish():
    return {"data": "These are the unpublished blogs"}


@app.get("/blog/{id}")
async def another(id:int):
    return {'data': id}



