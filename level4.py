#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python Coding Level4
    (http://www.pythonchallenge.com/pc/def/linkedlist.php)
"""


import urllib.request
import re


def main():
    """Main function"""

    # Find the first link
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    html = urllib.request.urlopen(base_url).read()

    ptn_first = re.compile(r'a href=".+?(\d{,5})"')
    matches = ptn_first.findall(html.decode('utf-8'))
    print("nothing=" + matches[0])

    # Repeat find link and jump to it
    ptn = re.compile(r'(\d+)$')
    if matches:
        while True:
            html = urllib.request.urlopen(base_url + '?nothing=' + matches[0]).read()
            matches = ptn.findall(html.decode('utf-8'))
            if not matches:
                break
            print("=> nothing=" + matches[0])
    print(html.decode('utf-8'))


if __name__ == "__main__":
    main()
