import requests
from datetime import datetime as dt
import os

NUTRI_APP_ID = os.environ["NUTRI_APP_ID"]
NUTRI_API_KEY = os.environ["NUTRI_API_KEY"]

nutri_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

nurti_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "Content-Type": "application/json"
}

nurti_params = {
     "query": input("What exercise did you do?: "),
     "gender": "male",
     "weight_kg": 80,
     "height_cm": 190,
     "age": 32
}

response = requests.post(url=nutri_url, headers=nurti_headers, json=nurti_params)

SHEETY_URL = os.environ["SHEETY_URL"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

exercise = response.json()["exercises"][0]["user_input"].title()
duration = round(int(response.json()["exercises"][0]["duration_min"]))
calories = response.json()["exercises"][0]["nf_calories"]

sheety_headers = {
    "Authorization": BEARER_TOKEN,
    "Content-Type": "application/json"
}

sheety_params = {
    "workout": {
        "date": str(dt.now().date()),
        "time": str(dt.now().time().strftime("%H:%M")),
        "exercise": exercise,
        "duration": str(duration),
        "calories": calories
  }
}

response2 = requests.post(url=SHEETY_URL, headers=sheety_headers, json=sheety_params)
print(response2.status_code)