from fastapi import FastAPI

app = FastAPI()


@app.get("/root")
def root():
    return {"Hello": "world"}


@app.get("/root/{item_id}")
def doc(item_id: int):
    return {"id": item_id}
