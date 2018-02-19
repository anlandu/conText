'''
Downloads the top 100 books on Project Gutenberg as text files
'''
import requests
from bs4 import BeautifulSoup
import re
r=requests.get("https://www.gutenberg.org/browse/scores/top#books-last30")
soup=BeautifulSoup(r.text, "html5lib")
top_100=[]
for n in range(100):
    book_tag=soup.find_all('ol')[4].find_all('li')[n].find('a')
    top_100.append([book_tag.text, book_tag['href']])
    book_title=top_100[n][0]
    book_title=book_title[:book_title.index("(")-1]
    try:
        book_page=requests.get("https://www.gutenberg.org{}".format(top_100[n][1]))
        book_soup=BeautifulSoup(book_page.text, "html5lib")
        txt_url=book_soup("td",text='Plain Text UTF-8')[0].a['href']
        book_txt=requests.get("http:{}".format(txt_url))
        with open("../resources/{}.txt".format(n), 'w+', encoding='utf-8') as f:
            f.write(book_title+"~~~"+book_txt.text)
    except:
        pass
