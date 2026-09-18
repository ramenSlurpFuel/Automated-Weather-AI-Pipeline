from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/")
def read_root():
    return {"message": "hello world"}

@app.get("/predict")
def predict(hour: int, day_of_year: int):
    input_df = pd.DataFrame([[hour, day_of_year]], columns=["hour", "day_of_year"])
    prediction = model.predict(input_df)
    return {"predicted_temperature": round(prediction[0], 1)}