import random
import requests
import uvicorn

from fastapi.responses import JSONResponse
from fastapi import FastAPI

from app.utils import convert_json_to_dict, proxy_number_to_words

from app.schemas import Number

app = FastAPI()


@app.post("/proxy_number_to_words")
def proxy_converter(number: Number):
    return JSONResponse(content=proxy_number_to_words(number=number))


@app.get("/test")
def start_test():
    """Автоматическое тестирование прокси-сервиса на 3 рандомных числах"""
    test_json = {}
    for _ in range(3):
        ubi_num_random = random.randint(1, 1000)
        response = requests.post(url="http://127.0.0.1:8000/convert", json={"ubi_num": ubi_num_random})
        response_dict = convert_json_to_dict(response=response)
        test_json[ubi_num_random] = response_dict.get("result")
    return JSONResponse(content=test_json)