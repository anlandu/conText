import json
import string
import requests
import nltk
nltk.download('punkt')
from nltk import RegexpTokenizer
import sys

def getAvgLength():
    try:
        getAvgLength("userInputtedBook")
    except:
        print("No book selected. Please run scripts/GetBookFromURL.py with a valid"+
        "Project Gutenberg txt URL before running this script.")
        sys.exit()


def getAvgLength(filename):
        try:
            with open("../resources/{}.txt".format(filename), 'r', encoding='utf-8', errors="ignore") as f:
                book_text=f.read()
                start=book_text.index(" ***")
                end=book_text.index("*** END OF THIS PROJECT GUTENBERG EBOOK")
                book_text=book_text[start+4:end]
                punctuation=string.punctuation+")’(,�--|"
                words=nltk.word_tokenize(book_text)
                num_words=0.0
                num_chars=0.0
                for word in words:
                    if word in punctuation:
                        pass
                    else:
                        num_words+=1.0
                        num_chars+=len(word)
                return (num_chars/num_words)
        except:
            print(filename)
            print("File not found! getAvgLength(filename) should only be called by CorpusWordLength.py. If you called getAvgLength() with a parameter,"+
            "please first download your desired text using GetBookFromURL, then call getAvgLength() without a parameter!")
            # sys.exit()
