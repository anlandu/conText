'''
Downloads the given URL as txt file
'''
import json
import string
import requests
import nltk
import sys

input=sys.argv[1]
try:
    input.index("www.gutenberg.org/files")
except:
    print("Invalid URL")
    sys.exit()
if input[-4:]!=".txt":
    print("Invalid URL")
    sys.exit()
try:
    res=requests.get(sys.argv[1])
    with open("../resources/userInputtedText.txt", 'w+', encoding='utf-8', errors="ignore") as f:
        f.write(res.text)
except:
    print("Invalid URL")
    sys.exit()
