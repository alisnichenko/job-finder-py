from src.web_request import get_source
from src.parse import parse_html
from src.parse import get_tags_jobs
import sys

def run() -> None:
    """
    The run function that accepts a website link from the shell
    and prints out the list of companies found on the website.

    Usage:
        python3 main.py <website> <spaced out keywords>
    Example:
        python3 main.py google.com/careers intern software students 
    """
    # Gets a set of keywords
    keywords = set([sys.argv[i] for i in range(2, len(sys.argv))])
    # Receives the source for the webpage.
    source = get_source(sys.argv[1]);
    # Checks the text for the keywords and gets the tags.
    links = get_links_jobs(source, keywords)
    print(elements_jobs)

if __name__ == "__main__":
    run()
