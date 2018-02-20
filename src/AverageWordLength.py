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

def getClosestLength(input):
    try:
        input.index("www.gutenberg.org/files")
    except:
        print("Invalid URL")
        sys.exit()
    if input[-4:]!=".txt":
        print("Invalid URL")
        sys.exit()
    try:
        res=requests.get(sys.argv[1])
        with open("../userBook.txt", 'w+', encoding='utf-8', errors="ignore") as f:
            f.write(res.text)
    except:
        print("Invalid URL")
        sys.exit()
    user_book_word_len=getAvgLength("userBook.txt").get("userBook.txt")
    closest_diff=9999
    for 

def getAllLengths():
    allLengths={}
    for book in os.listdir('../resources'):
        print(book)
        allLengths.update("resources/{}".format(AverageWordLength.getAvgLength(book)))
    print(allLengths)

def getAvgLength(filename):
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
                print("made it this far")
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
                num_words=0.0
                num_chars=0.0
                for word in words:
                    if word in punctuation:
                        pass
                    else:
                        num_words+=1.0
                        num_chars+=len(word)
                print({book_title:num_chars/num_words})
                return {book_title:num_chars/num_words}
        except:
            print()
            print("Error parsing file {}!".format(filename))
            # sys.exit()
