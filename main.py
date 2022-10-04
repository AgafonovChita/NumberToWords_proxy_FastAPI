import random
import requests

from fastapi.responses import JSONResponse
from fastapi import FastAPI

from app.utils import convert_to_json, convert_json_to_dict
from app.api import convert_number_to_words, create_xml_body
from app.schemas import Number

app = FastAPI()


@app.post("/convert")
def number_convert(number: Number):
    xml_body = create_xml_body(ubi_num=number.ubi_num)
    words_response = convert_number_to_words(data_xml=xml_body)
    response_json = convert_to_json(data_xml=words_response.content)
    return JSONResponse(content=response_json)


@app.get("/test")
def start_test():
    test_json = {}
    for _ in range(3):
        ubi_num_random = random.randint(1, 1000)
        response = requests.post(url="http://127.0.0.1:8000/convert", json={"ubi_num": ubi_num_random})
        response_dict = convert_json_to_dict(response=response)
        test_json[ubi_num_random] = response_dict.get("result")
    return JSONResponse(content=test_json)


