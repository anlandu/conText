import json
import string
import requests
from nltk import RegexpTokenizer
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import sys
import os
import csv
from bs4 import BeautifulSoup
import re
from collections import Counter

class AuthID:
    def loadText(url):
        if input[-4:]!=".txt":
            print("Invalid URL: Not a .txt file")
        try:
            res=requests.get(url)
            with open("../resources/userInputtedText.txt", 'w+', encoding='utf-8', errors="ignore") as f:
                f.write("USER CHOSEN BOOK~~~"+res.text)
        except:
            print("Error retrieving book")

    def writeStatsCSV(self):
            if os.path.exists("../book_stats.csv"):
                print("CSV exists")
                with open('../book_stats.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
                    reader = csv.reader(csv_file)
                #TODO: work on reading the data from CSV
            else:
                print("CSV does not exist")
                all_data={}
                for path, subdirs, files in os.walk("../resources"):
                    for name in files:
                        book_data=self.getStats(os.path.join(path, name))
                        all_data.update(book_data)
                fields=['book', 'author', 'chars', 'words', 'sentences', 'pauses', 'unique words', 'function words', 'content words', 'NN', 'IN', 'PRP', 'DT', 'NNP', 'RB', 'VBD', 'JJ', 'VB', 'CC']
                with open('../book_stats.csv', 'w+', encoding="utf-8", newline="", errors="ignore") as csv_file:
                    writer = csv.writer(csv_file)
                    wdict=csv.DictWriter(csv_file,fields,extrasaction='ignore')
                    writer.writerow(fields)
                    for key, value in all_data.items():
                        row={'book':key}
                        row.update(value)
                        wdict.writerow(row)
                return all_data

    def getStats(self, filename):
        with open(filename, 'r', encoding='utf-8', errors="ignore") as f:
            book_text=f.read()
            book_title=book_text[:book_text.index("~~~")]
            try:
                start=book_text.index("***\n")
            except:
                print(filename)
                start=0
            try:
                end=book_text.index("*** END OF ")
            except:
                try:
                    end=book_text.index("***END OF ")
                except:
                    print(filename)
                    end=len(book_text)
            author=filename[filename.index("resources\\")+10:filename.rfind("\\")]
            book_text=book_text[start+4:end]
            punctuation=string.punctuation+")’(,�--|"
            stopset=set(stopwords.words('english'))
            pauses=",;--—:"
            sents=sent_tokenize(book_text)
            words=word_tokenize(book_text)
            unique_words=set(words)
            num_sents=len(sents)
            num_words=0
            num_function_words=0
            num_stopwords=0
            num_chars=0
            num_pauses=0
            num_unique_words=len(unique_words)
            diff_words,diff_pos=zip(*pos_tag(words))
            all_nums=Counter(diff_pos)
            for word in words:
                if word in pauses:
                    num_pauses+=1
                elif word in punctuation:
                    pass
                else:
                    num_words+=1.0
                    num_chars+=len(word)
                    if word in stopset:
                        num_stopwords+=1
                    else:
                        num_function_words+=1
            all_nums.update({"words": num_words, "sentences": num_sents,
                "pauses": num_pauses, "function words": num_function_words,
                "content words": num_stopwords, "chars": num_chars,
                "unique words": num_unique_words, "author": author})
            print({book_title:all_nums})
            return {book_title:all_nums}
