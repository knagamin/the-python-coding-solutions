#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""The Python Challenge Level2 (http://www.pythonchallenge.com/pc/def/ocr.html)"""


import urllib.request
from bs4 import BeautifulSoup as BS
from bs4 import Comment


def main():

    count_dict = {}
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    html = urllib.request.urlopen(url).read()
    soup = BS(html, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for c in set(comments[1].strip()):
        count_dict[c] = comments[1].count(c)

    rare_chars = [ c for c in count_dict if count_dict[c] == 1 ]

    # print rare characters in order of appearance
    for c in comments[1]:
        if c in rare_chars:
                print(c, end="")

    print("")


if __name__ == "__main__":
    main()
