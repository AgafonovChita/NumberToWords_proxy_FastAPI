import random
import requests

from fastapi.responses import JSONResponse
from fastapi import FastAPI

from app.utils import proxy_number_to_words, test_api
from app.schemas import Number

app = FastAPI()


@app.post("/proxy_number_to_words")
def proxy_converter(number: Number):
    return JSONResponse(content=proxy_number_to_words(number=number))


@app.get("/test")
def start_test():
    """Автоматическое тестирование прокси-сервиса на 3 рандомных числах"""
    return JSONResponse(content=test_api())
