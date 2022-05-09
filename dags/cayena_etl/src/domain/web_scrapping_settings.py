from enum import Enum

class UrlConstants(Enum):
    INITIAL_PAGE_NUMBER: int = 1
    INITAL_PAGE_URL: str = "https://books.toscrape.com/catalogue/page-1.html"
    
class HTTPResponse(Enum):
    SUCCESSFUL_RESPONSE: int = 200