import nltk
import string
import requests
# nltk.download('punkt')
from nltk import RegexpTokenizer
import sys
import os
import csv
from collections import Counter
import csv
import itertools
import sys

'''
Write to CSV the Counter of parts of speech for each book
'''
def createCSVallPOS():
    all_books_POS={}
    for book in os.listdir('../resources'):
        print(book)
        all_books_POS.update(getPOS("resources/{}".format(book)))
        print("completed calculating sentence lengths successfully")
        fields=['book', 'NN', 'IN', 'PRP', 'DT', 'NNP', 'RB', 'VBD', 'JJ', 'VB', 'CC']
        with open('../book_POS.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            w=csv.writer(csv_file)
            wdict=csv.DictWriter(csv_file,fields,extrasaction='ignore')
            w.writerow(fields)
            for key,val in sorted(all_books_POS.items()):
                row={'book':key}
                row.update(val)
                wdict.writerow(row)

'''
Returns list of most frequent POS, along with each one's number of occurrences
'''
def getPOS(filename):
        try:
            with open("../{}".format(filename), 'r', encoding='utf-8', errors="ignore") as f:
                book_text=f.read()
                if book_text=="No text found":
                    return {book_title:999}
                book_title=book_text[:book_text.index("~~~")]
                try:
                    start=book_text.index("***\n")
                except:
                    start=0
                try:
                    end=book_text.index("*** END OF ")
                except:
                    try:
                        end=book_text.index("***END OF ")
                    except:
                        end=len(book_text)
                sents=nltk.sent_tokenize(book_text)
                num_sents=len(sents)
                book_text=book_text[start+4:end]
                punctuation=string.punctuation+")’(,�--|"
                words=nltk.word_tokenize(book_text)
                print("successfully tokenized")
                diff_words,diff_pos=zip(*nltk.pos_tag(words))
                pos_nums=Counter(diff_pos)
                # pos_freqs=nltk.pos_freq(words)
                print(pos_nums)
                return {book_title:pos_nums}
        except:
            print()
            print("Error parsing file {}!".format(filename))
            # sys.exit()
