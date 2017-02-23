import requests
from requests.auth import HTTPBasicAuth
import json


payload ={"applicationId": "32770", "name": "app1-conf", "description": "app1-conf", "ctlSchemaId": "32774"}

r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/saveConfigurationSchema', auth=HTTPBasicAuth('devhuang', 'devhuang'),  json=payload)
print r.text
