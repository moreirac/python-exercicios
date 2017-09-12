#!/usr/bin/env python3

import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"
location = "Ponte Hercilio Luz"
PARAMS = {'address': location}

resposta = requests.get(url = URL, params = PARAMS)

resp = resposta.json()

print(resp)

print(resp['results'][0]['formatted_address'])

