import requests
import os
from twilio.rest import Client

#https://api.openweathermap.org
my_api_key = ""

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

parameters = {

    "appid": my_api_key,
    "lat": 111111111111 # your lat,
    "lon": 111111111,
    "exclude": "daily,current,minutely"

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

weather_id = []
is_raining = False

weather_slice = data['hourly'][:12]

for id in weather_slice:
    weather_conditon = id['weather'][0]["id"]
    if weather_conditon < 700:
        is_raining = True

if is_raining:
    '''
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="your message",
        from_='',
        to=''
    )

    print(message.status)
    '''

    print("take your umberla")

'''
for id in range (0,12):

    id_wther = data['hourly'][id]['weather'][0]['id']
    weather_id.append(id_wther)

for id in weather_id:
    if id <700:
        print("Take your umbrala")
        break
'''
