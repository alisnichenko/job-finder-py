from web.selenium import selenium_script
from utilities.output import info
from utilities.webtools import get_links
from utilities.webtools import get_careers
import sys

def main() -> None:
    info("i", "Started main()...")
    url = sys.argv[1]
    src = selenium_script(url)
    links = get_links(src, "angel")
    careers = get_careers(links)
    info("d", careers)

if __name__ == "__main__":
    """
    I am not sure if that's how it's done in the industry, but that checks
    whether the url and url only was provided from the command line.
    """
    if (len(sys.argv) != 2):
        info("e", "Usage: python main.py [url]")
    else:
        main()