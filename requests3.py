#!/usr/bin/env python3

import time
import requests

parameters = {'lat': 37.78, 'lon': -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

resp = response.json()

print(resp['response'])

pos = 0
for resp_pass in resp['response']:
    pos = pos + 1
    print('%s: %s' % (str(pos), str(time.strftime('%Y-%m-%d %H:%M:%s', time.localtime(resp_pass['risetime'])))))

