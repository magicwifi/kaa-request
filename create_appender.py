import requests
from requests.auth import HTTPBasicAuth
import json


conf = {"mongoServers":[{"host":"localhost","port":27017}],"mongoCredentials":[],"dbName":"kaa","connectionsPerHost":{"int":30},"maxWaitTime":{"int":120000},"connectionTimeout":{"int":5000},"socketTimeout":{"int":0},"socketKeepalive":{"boolean":False},"includeClientProfile":{"boolean":False},"includeServerProfile":{"boolean":False}}





payload = {
    "pluginClassName":"org.kaaproject.kaa.server.appenders.mongo.appender.MongoDbLogAppender",
    "pluginTypeName":"MongoDB",
    "applicationId":"32770",
    "name":"My First Demo MongoDB log appender",
    "description":"My First Sample MngoDB log appender",
    "headerStructure":[
        "KEYHASH",
        "VERSION",
        "TIMESTAMP",
        "TOKEN",
        "LSVERSION"
    ],
    "maxLogSchemaVersion":2147483647,
    "minLogSchemaVersion":1,
    "jsonConfiguration":json.dumps(conf)    
}



r=requests.post('http://42.187.122.192:8080/kaaAdmin/rest/api/logAppender', auth=HTTPBasicAuth('devhuang', 'devhuang'),  json=payload)
print r.text
