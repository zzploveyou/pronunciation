# coding:utf-8
"""
get us pronunciation from
https://dictionary.cambridge.org/pronunciation/english
"""
from urllib.request import urlopen
import sys
from playsound import playsound
import re


def pro(word):
    word = word.strip()
    url = "https://dictionary.cambridge.org/pronunciation/english/{}".\
          format(word)
    content = urlopen(url).read()
    urls = set(re.findall('data-src-mp3="(.*?(uk|us)_pron.*?.mp3)', str(content)))
    for u, s in urls:
        # print("Now playing: pronunciation of {}".format(s))
        if s == 'us':
            playsound(u)


if __name__ == '__main__':
    try:
        word = sys.argv[1]
    except Exception as e:
        print("Usage: python pronun.py hello")
        print(("Error: {}".format(e)))
        sys.exit(1)
    pro(word)
