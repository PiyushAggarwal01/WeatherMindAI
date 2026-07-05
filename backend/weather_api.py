import requests


API_KEY = "6449d92367c356e68b49411e86f5ddeb"


def get_weather(city):

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )


    response = requests.get(url)

    data = response.json()


    print(data)   # DEBUG


    if response.status_code != 200:
        return {
            "error": data
        }


    weather = {

        "temp":
        data["main"]["temp"],

        "humidity":
        data["main"]["humidity"],

        "pressure":
        data["main"]["pressure"],

        "windspeed":
        data["wind"]["speed"]

    }


    return weather