import requests
from requests.auth import HTTPBasicAuth
import json
import shutil

payload=  {
"sdkProfileId":"32770",
"targetPlatform":"C"
}



r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/sdk', auth=HTTPBasicAuth('devhuang', 'devhuang'),  data=payload,stream=True)
if r.status_code == 200:
    with open('sdk-c.tar.gz', 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)        

