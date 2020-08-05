"""
Parsing the source code for the pages we received beforehand.
"""
from bs4 import BeautifulSoup as bs

def get_links_html(src: str, keywords: set) -> list:
    """
    Prettifies the source code of the page.
    """
    job_links = []
    soup = bs(src, 'html.parser')
    soup_text = soup.get_text()
    print(soup_text)
    return job_links
