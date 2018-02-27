import nltk
import string
import requests
nltk.download('punkt')
from nltk import RegexpTokenizer
import sys
import os
import csv
from collections import Counter

'''
Write to CSV the parts of speech for each book
'''
def getAllPOS():
    if os.path.exists("../book_POS.csv"):
        print("CSV exists")
        with open('../book_POS.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            all_books_POS=dict(reader)
        return all_books_POS

    else:
        print("CSV does not exist")
        all_books_POS={{}}
        for book in os.listdir('../testDir'):
            print(book)
            all_books_POS.update(getPOS("testDir/{}".format(book)))
        print("completed calculating sentence lengths successfully")
        with open('../book_POS.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in all_books_POS.items():
                writer.writerow([key, value])
        return all_books_POS

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
                return pos_nums
        except:
            print()
            print("Error parsing file {}!".format(filename))
            # sys.exit()
