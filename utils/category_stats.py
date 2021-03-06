#!/usr/bin/env python3

if __name__ == '__main__' and __package__ is None:
    import os
    # __file__ should be defined in this case
    PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.append(PARENT_DIR)

from utils import DatabaseDAO
import sys

full = len(sys.argv) == 2 and sys.argv[1] == "full"


def main():
    articles = DatabaseDAO.get_interesting()
    for category in DatabaseDAO.get_categories():
        identity = str(int(category["identity"]))
        cnt = 0
        print("-" * 20)
        print(category["name"])
        print("-" * 20)
        for article in articles:
            if "category" in article and identity in article["category"]:
                print(str(cnt) + " -- " + article["title"] + " " + str(article["category"]))
                print()
                if full:
                    print("Interest: " + str(article["interest"]))
                    print()
                    print(article["abstract"])
                    print()
                cnt += 1




if __name__ == "__main__":
    main()
