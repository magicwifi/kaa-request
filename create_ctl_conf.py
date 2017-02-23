import requests
from requests.auth import HTTPBasicAuth
import json

body=  {
     "type": "record",
     "name": "Configuration",
     "namespace": "org.kaaproject.kaa.schema.sample",
     "fields": [
         {
             "name": "samplePeriod",
             "type": "int",
             "by_default": 1
         }
     ]
 }




payload ={"body":json.dumps(body), "tenantId" : "3","applicationToken" : "72539440111373153773"}

r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/CTL/saveSchema', auth=HTTPBasicAuth('devhuang', 'devhuang'),  data=payload)
print r.text
