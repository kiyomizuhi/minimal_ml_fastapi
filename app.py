from fastapi import FastAPI, HTTPException

from model import InCircleClassifier


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, world!"}


@app.post("/predict_incircle")
def predict_incircle(X, Y):
    X = float(X)
    Y = float(Y)
    if type(X) != float:
        raise HTTPException(
            status_code=400,
            detail = "Please Provide a valid input for X!!!!"
            )

    if type(Y) != float:
        raise HTTPException(
            status_code=400,
            detail = "Please Provide a valid input for Y!!!!"
            )

    pred = InCircleClassifier().predict([X, Y])
    print("kaka", pred)
    return {
        "answer": "in" if pred else '"out'
        }