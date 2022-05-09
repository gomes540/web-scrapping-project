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

def get_all_desired_info(soup: str, name: str, target_class: str) -> List[str]:
  all_info = soup.find_all(name, class_=target_class)
  print(f"fetched {len(all_info)} informations")
  return all_info

def get_book_title(book_info) -> str:
  title = book_info.h3.a.get('title')
  return title

def get_book_price(book_info) -> str:
  price = book_info.find("p", class_="price_color").text[2:]
  return price

def get_book_rating(book_info) -> str:
  rating = book_info.p.get("class")[1]
  return rating

def get_all_books_in_website(all_valid_urls: List[str]) -> List[str]:
  all_books_information = []
  for page_url in all_valid_urls:
    soup = get_and_parse_url(page_url)
    books_in_page = get_all_desired_info(soup, "article", "product_pod")
    all_books_information+=books_in_page
  return all_books_information

def get_title_name_price_lists(all_books_information: List[str]) -> List:
  all_books_title = []
  all_books_rating = []
  all_books_price = []
  for book in all_books_information:
    all_books_title.append(get_book_title(book))
    all_books_rating.append(get_book_rating(book))
    all_books_price.append(get_book_price(book))
  return all_books_title, all_books_rating, all_books_price

def count_books_copies(all_tiles: List[str]) -> dict:
  copies_num = dict(Counter(all_tiles))
  return copies_num

def create_copies_dataframe(repeted_books: dict) -> pd.DataFrame:
  copies_dataframe = pd.DataFrame.from_dict(repeted_books, orient='index', columns = ["copies"]).rename_axis('title').reset_index()
  return copies_dataframe

def save_dataframe_as_csv(dataframe: pd.DataFrame, local_path: str) -> None:
  dataframe.to_csv(local_path, index=False)