import json
from dict2xml import dict2xml

with open('payload.json') as json_payload:
    data = json.load(json_payload)

    print(dict2xml(data, wrap="all", indent=" "))
