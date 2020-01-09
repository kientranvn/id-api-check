import requests
import json

url = "http://163.44.207.75:5050/idfull/v1/recognition"

headers = {
    'api-key': 'e42135e3-f9bb-4b1e-98d6-3a5020fbf2a4'
}

payload = {
    'encode': '1'
}

files = [
  ('image1', open('C:/Workspace/api_testing/ID_1_F.jpg','rb')),
  ('image2', open('C:/Workspace/api_testing/ID_1_B.jpg','rb'))
]

response = requests.post(url, headers = headers, data = payload, files = files)


data = response.json()
print(data['address']['score'])
print(data['address']['text'])

#print(response.text.encode('utf8'))
