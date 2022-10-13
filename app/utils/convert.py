import json
from requests.models import Response
import xmltodict
from typing import Dict
from app.schemas import Number
from app.api import create_xml_body, original_number_to_words


def proxy_number_to_words(number: Number):
    return converter(original_number_to_words)(number)


def converter(original_method):
    def wrapper(number: Number):
        xml_body = create_xml_body(ubi_num=number.ubi_num)
        response = original_method(data_xml=xml_body)
        response_json = convert_to_json(data_xml=response.content)
        return response_json
    return wrapper


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



