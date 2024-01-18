# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:13:47 2023

@author: konst
"""
import json
import requests

url_get = 'https://api.mcs3.miele.com/v1/devices'
url_on = 'https://api.mcs3.miele.com/v1/devices/000184392486/actions'

headers_get = {'accept': 'application/json; charset=utf-8', 'Authorization': 'Bearer DE_91675cb2e163ba73608754a7c9274d8a'}   
headers_on = {'accept': '*/*', 'Authorization': 'Bearer DE_91675cb2e163ba73608754a7c9274d8a', 'Content-Type': 'application/json'}
data = {'powerOff': True}
json_data = json.dumps(data)

#r = requests.get(url_get, headers=headers_get)
r = requests.put(url_on, headers=headers_on, data=json_data)

print(r)

#pretty_json = json.loads(r.text)
#print(json.dumps(pretty_json, indent=2))
