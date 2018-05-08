'''
Downloads the top 100 books on Project Gutenberg as text files
'''
import pathlib
import requests
from bs4 import BeautifulSoup
import re
r=requests.get("https://www.gutenberg.org/browse/scores/top#authors-last30")
soup=BeautifulSoup(r.text, "html5lib")
author_urls=[]
books=[]

'''
Parses the top authors from last 30 days; for each, finds all English texts,
finds those books' txt files and downloads them
'''
for n in range(100):
    author_tag=soup.find_all('ol')[5].find_all('li')[n].find('a')
    author_urls.append([author_tag.text, author_tag['href']])
    author_name=author_urls[n][0]
    author_name=author_name[:author_name.index("(")-1]
    author_href=author_urls[n][1]
    author_href=author_href[author_href.rfind('/')+3:]
    print(author_href)
    author_page=requests.get("https://www.gutenberg.org{}".format(author_urls[n][1]))
    author_soup=BeautifulSoup(author_page.text, "html5lib")
    books_temp=author_soup.find('a', {"name":author_href})
    books_temp=books_temp.find_next('ul').find_all('li', {"class":"pgdbetext"})
    for book in books_temp:
        if "(English)" in book.text and "(as Editor" not in book.text
        and "(as Translator" not in book.text:
            books.append(book)
    n=0
    for book in books:
        try:
            book_title=book.text[:book.text.index("(")-1]
            book_url=book.find('a')['href']
            book_page=requests.get("https://www.gutenberg.org{}".format(book.find('a')['href']))
            book_soup=BeautifulSoup(book_page.text, "html5lib")
            txt_url=book_soup("td",text='Plain Text UTF-8')[0].a['href']
            book_txt=requests.get("http:{}".format(txt_url))
            pathlib.Path("../resources/{}".format(author_name)).mkdir(parents=True, exist_ok=True)
            with open("../resources/{}.txt".format(author_name+"/"+str(n)), 'w+', encoding='utf-8') as f:
                f.write(book_title+"~~~"+book_txt.text)
        # if .txt link is not found, just pass
        except:
            pass
        n+=1
    books=[]
