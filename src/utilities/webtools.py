# The top import gives pylint error, but it works fine.
from .output import info
from bs4 import BeautifulSoup
import requests
import re
import os

def get_links(src: str, unwanted_keyword = "") -> list():
    """
    Takes source code as a parameter, parses it, and extract all the links
    that are presented in the source code provided.
    
    Args:
        src: a string parameter containing source of the page.
        wanted_keyword: a string that is desired in the results.
        unwanted_keyword: a string that is not desired in obtained urls.
    Returns:
        A list with all http:// and https:// links on the page.
    """
    info("i", "Started get_links() with unwanted_keyword " + unwanted_keyword)
    links = []
    soup = BeautifulSoup(src, 'html.parser')
    href_soup = soup.findAll('a', attrs={'href': re.compile("^http(s)?://")})
    # links = [link.get('href') for link in href_soup if "angel" not in link]
    for link in href_soup:
        url = link.get('href')
        if unwanted_keyword not in url or unwanted_keyword is "":
            links.append(url)
    info("i", "Exiting get_links().")
    return links

def get_careers(links: list) -> list():
    """
    Iterates through every website in a links list, appends careers() and
    looks for html <a> tags that contain words "Intern" or "Internship"
    inside, and then, if that's the case, appends it to the return list.

    Args:
        links: list of company websites and their base urls.
    Returns:
        A list of urls from the positions that contain "Intern" in them.
    """
    info("i", "Started get_careers()...")
    careers = []
    for link in links:
        if link[-1] is not '/':
            link += "/"
        info("i", "Trying " + link + "careers")
        try:
            page = requests.get(link + "careers").text
            soup = BeautifulSoup(page, 'html.parser')
            href_soup = soup.findAll('a', attrs={'href': re.compile("^http(s)?://")})
            for href in href_soup:
                if "ntern" in href.text:
                    info("i", "Added one link from " + href + " With text " + href.text)
                    careers.append(href.get('href'))
        except:
            info("i", "link " + link + " threw an error. Continuing...")
            continue
    return careers
        