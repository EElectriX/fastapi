from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index(limit,published):
    return {"message": f"Hello World: {limit} blogs from the database"}

@app.get("/about")
def about():
    return {"message": "This is a FastAPI application"}

@app.get("/blog/unpublished")
def unpublished():
    return {"message": "Unpublished blog posts"}


@app.get("/blog/{id}")
def blog(id: int):
    return {"message": f"Blog post {id}"}

@app.get("/blog/{id}/comments")
def comment(id):
    return {"data": {'1','2'}}


