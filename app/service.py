from fastapi import FastAPI

app = FastAPI()

@app.get("/book")
def book_ambulance():
    return {"message": "Ambulance booking successfullllllll"}