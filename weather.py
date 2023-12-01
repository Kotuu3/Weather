#!/usr/bin/env python3

import requests
import time
import random
import json


api_key = "Your api key goes here"

#for example: city = "Warsaw,PL"
city = "City,Country"

lang = "en"


#custom messages showed under forecast
messages = [
    "Stay Hydrated!",
    "Hey! What's up? :3",
    "Have a good day!"
]

random_message = random.choice(messages)



def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15


def get_data(api):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},uk&lang={lang}&APPID={api_key}")
    if response.status_code == 200:
        data = response.json()

        temp_celsius = kelvin_to_celsius(data['main']['temp'])


        print(f"Miasto: {data['name']}")
        print(f"Temperatura: {temp_celsius:.2f} °C")
        print(f"Ciśnienie: {data['main']['pressure']} hPa")
        print(f"Wilgotność: {data['main']['humidity']}%")
        print(f"Warunki: {data['weather'][0]['description']}")
        print("===========")
        print(random_message)

    else:
        print(response.status_code)




while True:
    get_data(api_key)
    time.sleep(600)

