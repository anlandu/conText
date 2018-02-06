import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.gutenberg.org/browse/scores/top#books-last30")
soup=BeautifulSoup(r.text, "html5lib")
top_100=[]
for n in range(100):
    top_100.append([i['href'] for i in soup.find_all('li')[n].find_all('a')])
    with open("{}.txt".format(n), 'w+') as f:
        book=requests.get("https://www.gutenberg.org{}".format(top_100[n][0]))
        # txturl=[i['href'] for i in book.find_all('td').find_all('text/plain')]
        print(book.text)
        f.write(book.text)
