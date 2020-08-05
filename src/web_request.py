"""
This file contains logic related to requests and browsing.
The functions in this file are getting called from the main.py
"""
import requests

def get_source(website: str) -> str:
    """
    This function uses the requests library to get the source code
    of the webpage. Address of the webpage is passed to the function.
    Arguments:
        website: string value of the website in question.
    Returns:
        source code of the website as a string.
    """
    response = requests.get(website)
    return response.content

