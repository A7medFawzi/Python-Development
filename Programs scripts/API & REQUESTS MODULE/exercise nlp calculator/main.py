import requests
from datetime import datetime


#You can fill out this data through this link
#https://www.nutritionix.com/business/api

APP_ID = ""
API_KEY = ""
API_ENDPOINT = ""
#https://developers.google.com/sheets/api
SHEET_API_POINT = ""

HEADERS = {

    "x-app-id": APP_ID,
    "x-app-key": API_KEY

}

paramters = {

    "query": input("what excrise did you do?: "),
    "gender": "your gender",
    "weight_kg": 85,
    "height_cm": 190,
    "age":30

}

response = requests.post(url=API_ENDPOINT, json=paramters, headers=HEADERS)
response.raise_for_status()
data = response.json()

today_time = datetime.now().time()
today_time = today_time.strftime("%H:%M:%S")

today_date = datetime.now().date()
today_date = today_date.strftime("%d-%m-%Y")

for ex in data['exercises']:

    user_exercise = ex['name']
    exercise_time = ex['duration_min']
    burned_cal = ex['nf_calories']
    sheet_paramters = {

        "workout": {

            "date": today_date,
            "time": today_time,
            "exercise": user_exercise.title(),
            "duration": round(exercise_time),
            "calories": round(burned_cal)

        }

    }

    sheet_response = requests.post(SHEET_API_POINT, json=sheet_paramters, auth=("", ""))

    print(sheet_response.text)
