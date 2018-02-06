import json
import string
import requests
import nltk
import sys

res=requests.get(sys.argv[1])
i=res.text.index(" ***")
text=res.text[i+4:]
print(text[:100])
