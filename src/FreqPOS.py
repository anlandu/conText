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
INCOMPLETE
'''
def getAllPOS():
    if os.path.exists("../book_sent_lens.csv"):
        print("CSV exists")
        with open('../book_POS.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            all_lengths=dict(reader)
        return all_lengths

    else:
        print("CSV does not exist")
        all_lengths={}
        for book in os.listdir('../resources'):
            print(book)
            all_lengths.update(getAvgLength("resources/{}".format(book)))
        print("completed calculating sentence lengths successfully")
        with open('../book_POS.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in all_lengths.items():
                writer.writerow([key, value])
        return all_lengths

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
