from urllib.request import Request
from bs4 import BeautifulSoup, ResultSet
from typing import List, Optional
import pydantic
import pdb


class Image(pydantic.BaseModel):
    source: str
    alternative: str


class News(pydantic.BaseModel):
    title: str
    url: str
    img: Optional[Image] = None
    text: Optional[str] = None


ROOT_URL = "https://www.jpl.nasa.gov/news"


def parsing_request(request_object: Request) -> BeautifulSoup:
    return BeautifulSoup(request_object.text, "html.parser")


def generate_url_next_page(url: str, page=1) -> str:
    if int(page) <= 1:
        return url[:34]
    page = str(page)
    return url[:34] + "/page/" + page


def get_news_nasa(soup: BeautifulSoup) -> dict:
    block_news = soup.find_all()

    result_news = [News(
        # title=item.find("div", class_="blog-post-card__info").find("a").text,
        # url=ROOT_URL +
        #     item.find("div", class_="blog-post-card__info").find("a").get('href'),
        # img=Image(
        #     source=item.find("img").get('src'),
        #     alternative=item.find("img").get("alt")
        ),
    # )
        # for item in block_news
    ]

    return result_news