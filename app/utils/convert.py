import json
from requests.models import Response
import xmltodict
from typing import Dict


def convert_json_to_dict(response: Response) -> Dict:
    """
    :param response: request.Response from API
    :return: response-dict
    """
    return json.loads(response.json())


def convert_to_json(data_xml: str) -> "json-str":
    """
    :param data_xml: XML-response from API
    :return: response converted to json
    """
    data_dict = xmltodict.parse(data_xml)
    result_dict = get_words_from_response(response=data_dict)
    result_json = json.dumps(result_dict)
    return result_json


def get_words_from_response(response: Dict) -> Dict:
    """Достаём текст ответа (текстовое представление числа)"""
    words = response.get("soap:Envelope").\
        get("soap:Body").\
        get("m:NumberToWordsResponse").\
        get("m:NumberToWordsResult")
    return {"result": words}



