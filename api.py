import requests
import json

protocol = 'https'
host = '192.168.206.132'
port = '9200'
user = 'admin'
password = 'SecretPassword'
endpoint = '/_search'
base_url = f"{protocol}://{host}:{port}{endpoint}"

headers = {
   'Content-Type': 'application/json'
}

auth = (user,password)

'''
{ 
    "query": 
        { "bool": 
            { "must": [ 
                {"term": { "agent.ip": "192.168.206.133"}} 
              ] 
            } 
        },
    "sort": [ 
        { "timestamp": { "order": "desc" } } 
    ], 
    "size": 1 
}
'''

data = '{ "query": { "bool": { "must": [ {"term": { "agent.ip": "192.168.206.133"}} ] } },"sort": [ { "timestamp": { "order": "desc" } } ], "size": 1 }'

request_result = requests.post(url = base_url, data = data, auth = auth, verify = False, headers = headers)

def parser(request_result):
    tmp = json.loads(request_result.content.decode())
    return tmp['hits']['hits'][0]['_source']['rule']['mitre']['technique']

print()
print('technique: '+str(parser(request_result)))
