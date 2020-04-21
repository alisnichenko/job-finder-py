# from src.webscraper import get_links
from src.webscraper import get_links
# from src.webscraper import follow_link
# from src.telegram import message_links
import sys

def main() -> None:
    if (len(sys.argv) != 2):
        print("[ERROR] Usage: python main.py [website with a list of companies]")
    else:
        print("[INFO] Calling get_links()...")
        links_list = get_links(sys.argv[1])
        print(links_list)
    
    print("[INFO] Exiting main()...")


if __name__ == "__main__":
    main()