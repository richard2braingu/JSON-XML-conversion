import json
import xmltodict

with open('payload.xml') as xml_payload:
    data = xmltodict.parse(xml_payload.read())

    print(json.dumps(data))