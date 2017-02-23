import requests
from requests.auth import HTTPBasicAuth

payload = {'name': 'app1', 'tenantId': '3'}
r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/application', auth=HTTPBasicAuth('huangzhe1218', 'huangzhe1218'),  json=payload)
print r.text
