import requests
from requests.auth import HTTPBasicAuth
r=requests.get('http://42.187.122.192:8080/kaaAdmin/rest/api/tenants', auth=HTTPBasicAuth('admin', 'admin123'))
print r.text
