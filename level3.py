#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python Coding Level3
    (http://www.pythonchallenge.com/pc/def/equality.html)
"""


import urllib.request
import re
from bs4 import BeautifulSoup as BS
from bs4 import Comment


def main():
    """Main function"""
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    html = urllib.request.urlopen(url).read()
    soup = BS(html, 'html.parser')
    comment = soup.find_all(string=lambda text: isinstance(text, Comment))[0]

    pattern = re.compile(r'(?<=[^A-Z][A-Z]{3})([a-z])[A-Z]{3}[^A-Z]')
    matches = pattern.findall(comment)
    print(("").join(matches))

if __name__ == "__main__":
    main()
