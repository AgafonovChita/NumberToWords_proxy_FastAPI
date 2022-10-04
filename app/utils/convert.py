import dict2xml
import json
from typing import Dict
import requests


def json_to_xml(data_json: Dict) -> "xml_string":
    data_dict = json.loads(data_json)
    data_xml = dict2xml.dict2xml(data=data_dict,
                                 indent="  ")
    return data_xml


# def convert_test():
#     page = requests.get('https://quandyfactory.com/api/example')
#     content = page.json()
#     print(type(content))
#     print(content)
#     data_xml = dict2xml.dict2xml(data=content,
#                                  indent="  ")
#     print(type(data_xml))
#     print(data_xml)



