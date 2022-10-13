import random
import requests

from app.utils import convert_json_to_dict


def test_api():
    """автоматическое тестирование proxy на 3 рандомных числах"""
    test_json = {}
    for _ in range(3):
        ubi_num_random = random.randint(1, 1000)
        response = requests.post(url="http://127.0.0.1:8000/proxy_number_to_words", json={"ubi_num": ubi_num_random})
        response_dict = convert_json_to_dict(response=response)
        test_json[ubi_num_random] = response_dict.get("result")
    return test_json
