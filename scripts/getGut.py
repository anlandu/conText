import requests
from bs4 import BeautifulSoup
import re
r=requests.get("https://www.gutenberg.org/browse/scores/top#books-last30")
soup=BeautifulSoup(r.text, "html5lib")
top_100=[]
for n in range(100):
    top_100.append([i['href'] for i in soup.find_all('li')[n].find_all('a')])
    with open("{}.txt".format(n), 'w+', encoding='utf-8') as f:
        book=requests.get("https://www.gutenberg.org{}".format(top_100[n][0]))
        booksoup=BeautifulSoup(book.text, "html5lib")
        txturl=booksoup("td",text='Plain Text UTF-8')
        try:
            url=txturl[0].a['href'][2:]
            booktxt=requests.get("http://{}".format(url))
            f.write(booktxt.text)
        except:
            f.write("No text found")
