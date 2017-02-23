import requests
from requests.auth import HTTPBasicAuth
import json


payload={
  "configurationSchemaVersion": 2,
  "profileSchemaVersion": 0,
  "notificationSchemaVersion": 1,
  "logSchemaVersion": 2,
  "name": "MyfirstSDK",
  "applicationId": "32770",
  "endpointCount": 0
}


r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/createSdkProfile', auth=HTTPBasicAuth('devhuang', 'devhuang'),  json=payload)
print r.text
