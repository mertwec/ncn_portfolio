import requests
import time

def make_request(url_path):
    return requests.get(url_path)

def get_page(url_path):
    resp = make_request(url_path)
    if resp.status_code == 200:
        return
    return True

def white_time(time_in_min):
    time.sleep(time_in_min*60)

def get_page_every_time(url_page, time_white):
    while 1:
        white_time(time_white)
        try:
            get_page(url_page)
        except requests.exceptions.InvalidSchema:
            print(f"NoConnect to {url_page}")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    path_local = "http://localhost:8000/mock/"
    path_project = "https://valoliin.onrender.com/mock/"
    render_com = 14.9
    get_page_every_time(path_local, render_com)
    