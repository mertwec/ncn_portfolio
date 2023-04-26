import requests
import os
from requests.models import Response, Request
from requests.auth import HTTPBasicAuth
from typing import Union

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    #             'Mozilla/5.0(X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0 Chrome/103.0.5060.134 Safari/537.36'
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    # 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
}

proxies = {
    # 'http': "",
    # 'https': ""
}


def get_request(read_url: str, headers=headers, proxies=proxies) -> Union[Response, str]:
    try:
        response = requests.get(
            read_url,
            headers=headers,
            proxies=proxies,
            timeout=3,
        )

        if response.status_code == 200:
            return response
        return f"Unsucces request: {response.status_code}"
    except Exception as e:
        return e


def basic_auth(url: str, user, login, headers=headers, proxies=proxies) -> Response:
    try:
        response = requests.get(
            url,
            auth=HTTPBasicAuth(user, login),
            headers=headers,
            proxies=proxies
        )
        if response.status_code == 200:
            return response
        return f"Unsucces request: {response.status_code}"
    except Exception as e:
        return e


def send_to_telegram(message, apiToken: str, chatID: int) -> Response | str:
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try:
        response = requests.post(
            apiURL, json={'chat_id': chatID, 'text': message})
        if response.status_code == 200:
            return response
        return f"Unsucces request: {response.status_code}"
    except Exception as e:
        return e


def get_image(images_url, path_to_save, name_img):
    img_data = requests.get(images_url).content 
    with open(os.path.join(path_to_save, name_img), 'wb') as handler: 
        handler.write(img_data) 
