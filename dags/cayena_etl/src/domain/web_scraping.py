import requests
from bs4 import BeautifulSoup
from collections import Counter
from typing import List
import pandas as pd
from web_scrapping_settings import UrlConstants, HTTPResponse, Parser

def get_all_valid_urls() -> List[str]:
    valid_urls = []
    num_page = UrlConstants.INITIAL_PAGE_NUMBER.value
    base_url = UrlConstants.INITAL_PAGE_URL.value
    while requests.get(base_url).status_code == HTTPResponse.SUCCESSFUL_RESPONSE.value:
        valid_urls.append(base_url)
        num_page+=1
        base_url = f"https://books.toscrape.com/catalogue/page-{num_page}.html"
    print(f"{len(valid_urls)} fetched valid pages")
    return valid_urls

def get_and_parse_url(url: str) -> str:
    result = requests.get(url)
    soup = BeautifulSoup(result.text, Parser.HTML_PARSER)
    return soup
    