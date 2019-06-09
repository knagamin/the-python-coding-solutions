#!/usr/bin/env python3
#-*- coding: utf-8
"""The Python Coding Level1"""


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    for c in s:
        if c in alphabet:
            rotted_idx = (ord(c) - ord('a') + 2) % len(alphabet)
            print(alphabet[rotted_idx], end="")
        else:
            print(c, end="")

    print("")
