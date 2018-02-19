'''
Returns the averge word length of a given .txt file
'''
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
            with open("../resources/{}".format(filename), 'r', encoding='utf-8', errors="ignore") as f:
                book_text=f.read()
                if book_text=="No text found":
                    return {book_title: 999}
                book_title=book_text[:book_text.index("~~~")]
                start=book_text.index("***\n")
                print("made it this far")
                try:
                    end=book_text.index("*** END OF ")
                except:
                    end=book_text.index("***END OF ")
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
                return {book_title:num_chars/num_words}
        except:
            print()
            print("Error parsing file {}!".format(filename))
            # sys.exit()
