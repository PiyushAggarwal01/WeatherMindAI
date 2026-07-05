from fastapi import FastAPI
import pickle
import numpy as np
from backend.weather_api import get_weather
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Load Model
# ---------------------------

model = pickle.load(
    open(
        "model/weather_model.pkl",
        "rb"
    )
)


# Check model required features

print(
    "Model Required Features:",
    model.n_features_in_
)


# ---------------------------
# Load Scaler
# ---------------------------

scaler = pickle.load(
    open(
        "model/scaler.pkl",
        "rb"
    )
)


print(
    "Scaler Required Features:",
    scaler.n_features_in_
)



@app.get("/")
def home():

    return {

        "message":
        "WeatherMind AI Running",

        "model_features":
        model.n_features_in_

    }



@app.post("/predict")
def predict_weather(

    temp: float,
    humidity: float,
    windspeed: float,
    pressure: float

):


    data = np.array(

        [[

            temp,
            humidity,
            windspeed,
            pressure

        ]]

    )


    print(
        "Input Shape:",
        data.shape
    )


    scaled_data = scaler.transform(
        data
    )


    prediction = model.predict(
        scaled_data
    )


    return {

        "Tomorrow Temperature":

        round(

            float(prediction[0]),

            2

        )

    }
@app.get("/predict_city/{city}")
def predict_city(city:str):


    weather = get_weather(city)


    if "error" in weather:

        return weather


    data = np.array(
        [[
            weather["temp"],
            weather["humidity"],
            weather["windspeed"],
            weather["pressure"]
        ]]
    )


    scaled = scaler.transform(data)


    prediction = model.predict(scaled)


    return {

        "city": city,

        "current_weather": weather,

        "Tomorrow Prediction":

        round(
            float(prediction[0]),
            2
        )

    }