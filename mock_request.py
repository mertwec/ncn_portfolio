import logging
import os
import threading
import time

import requests

base_dir: str = os.path.dirname(__file__)

logging.basicConfig(
    filename=os.path.join(base_dir, "log_mock_request.txt"),
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s: [%(url_path)s] %(message)s",
)


def get_page(url_path):
    try:
        resp = requests.get(url_path)
        if resp.status_code == 200:
            logging.info("Ok", extra={"url_path": url_path})
        else:
            logging.error(f"status code:{resp.status_code}", extra={"url_path": url_path})
    except requests.exceptions.InvalidSchema as ie:
        logging.error(f"{ie}", extra={"url_path": url_path})
    except Exception as e:
        logging.critical(f"{e}", extra={"url_path": url_path})


def white_time_minutes(time_in_min):
    time.sleep(time_in_min * 60)


def get_page_every_time(url_path, time_waite):
    logging.info("Start queries", extra={"url_path": url_path})
    while 1:
        get_page(url_path)
        white_time_minutes(time_waite)


if __name__ == "__main__":
    path_local = "http://localhost:8000/mock/"
    path_project = "https://valoliin.onrender.com/mock/"
    # path_project2 = "https://spa-comments.onrender.com/users/login/"
    time_waite = 14.7

    th1 = threading.Thread(target=get_page_every_time, args=(path_project, time_waite))
    # th2 = threading.Thread(target=get_page_every_time, args=(path_project2, time_white))

    th1.start()
    # th2.start()
