#!/usr/bin/env python3

import requests

API_ENDPOINT = "http://pastebin.com/api/api_post.php"
API_KEY = "e1af706fba81a9806f32a4a9cef6c3fa"

source_code = "GIROPOPS STRIGUS GIRUS"

data = {'api_dev_key': API_KEY, 'api_option': 'paste', 'api_paste_code': source_code, 'api_paste_format': 'python'}

response = requests.post(url = API_ENDPOINT, data = data)

print(response.status_code)
print(response.url)
resposta = response.text

print("A url do erro/codigo eh a seguinte: %s" % resposta)




