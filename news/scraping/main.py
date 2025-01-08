from tools.scraping_tesmanian import (ROOT_URL, get_news_tasmania,
                                      parsing_request)
from tools.tool_requests import get_request


def get_news():
    page = get_request(ROOT_URL)
    soup = parsing_request(page)
    out = get_news_tasmania(soup)
    return out 

if __name__ == "__main__":
   print(get_news())
