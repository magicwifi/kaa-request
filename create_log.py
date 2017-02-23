import requests
from requests.auth import HTTPBasicAuth
import json


payload ={"applicationId": "32770", "name": "app1-log", "description": "app1-log", "ctlSchemaId": "32773"}

r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/saveLogSchema', auth=HTTPBasicAuth('devhuang', 'devhuang'),  json=payload)
print r.text
