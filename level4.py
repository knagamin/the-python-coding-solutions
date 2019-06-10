#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The Python Coding Level4
    (http://www.pythonchallenge.com/pc/def/linkedlist.php)
"""


import urllib.request
import re

BASE_URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
MESSAGE = "Yes. Divide by two and keep going."


def main():
    """Main function"""

    # Find the first link
    html = urllib.request.urlopen(BASE_URL).read()
    ptn_first = re.compile(r'a href=".+?(\d{,5})"')
    matches = ptn_first.findall(html.decode('utf-8'))
    print("nothing=" + matches[0])

    # Repeat find link and jump to it
    ptn = re.compile(r'(\d+)$')
    if matches:
        num = matches[0]
        while True:
            html = urllib.request.urlopen(BASE_URL + '?nothing=' + num).read()
            matches = ptn.findall(html.decode('utf-8'))
            if html.decode('utf-8') == MESSAGE:
                print(html.decode('utf-8'))
                num = str(int(num)//2)
            elif not matches:
                break
            else:
                num = matches[0]
            print("=> nothing=" + num)
    print(html.decode('utf-8'))


if __name__ == "__main__":
    main()
