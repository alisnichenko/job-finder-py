from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import re
import os

def get_links(given_url: str) -> list():
    origin = os.path.dirname(str)
    referer = origin + '/companies'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' +
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/54.0.2840.90 Safari/537.36',
        'Origin': origin,
        'Referer': referer + '/companies'
    }
    # Sending a get request
    html_doc = requests.get(given_url, headers=headers).textS
    soup = BeautifulSoup(html_doc, 'html.parser')
    href_soup = soup.findAll('a', attrs={'href': re.compile("^http(s)?://")})
    links = [link.get('href') for link in href_soup]

    return links