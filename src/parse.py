"""
Parsing the source code for the pages we received beforehand.
"""
from bs4 import BeautifulSoup as bs
import re

def get_links_html(src: str, keywords: set) -> list:
    """
    Prettifies the source code of the page.
    """
    match_elements, job_links = set(), []
    soup = bs(src, 'html.parser')
    for keyword in keywords:
        for element in soup(text=re.compile(keyword)):
                match_elements.add(element)

    # Prints out matched position titles.
    for match in match_elements:
        print(match.parent.text)
    return job_links
