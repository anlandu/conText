'''
Methods to generate average sentence length of a file, create file containing
average sent lengths of all files in a directory, and given a Project Gutenberg
URL, return the text with the closest average sentence length'''
import string
import requests
import nltk
nltk.download('punkt')
from nltk import RegexpTokenizer
import sys
import os
import csv
from collections import OrderedDict
'''
Given a Project Gutenberg URL, get the book (out of top 100 on Project Gutenberg)
with the closest average sentence length
'''
def getClosestPauses(input):
    try:
        input.index("www.gutenberg.org/")
    except:
        print("Invalid URL: not a Gutenberg URL")
        sys.exit()
    if input[-4:]!=".txt":
        print("Invalid URL: does not end in txt")
        sys.exit()
    try:
        print(input)
        res=requests.get(input)
        with open("../userBook.txt", 'w+', encoding='utf-8', errors="ignore") as f:
            f.write("User Chosen Text~~~"+res.text)
    except:
        print("Invalid URL")
        sys.exit()
    user_book_pauses=getAvgPause("userBook.txt").get("User Chosen Text")
    diffs={}
    all_book_pauses=getAllPauses()
    for title, avg_pauses in all_book_pauses.items():
        diff=abs(user_book_pauses-float(avg_pauses))
        diffs.update({title:diff})
    sorted_diffs=OrderedDict(sorted(diffs.items(), key=lambda t: t[1]))
    return "Books with closest average sentence length: " + str(sorted_diffs)

'''
Read or, if non-existent, create a CSV of the average sentence lengths of all of the
top 100 books
'''
def getAllPauses():
    if os.path.exists("../book_sent_lens.csv"):
        print("CSV exists")
        with open('../book_sent_lens.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            all_pauses=dict(reader)
        return all_pauses

    else:
        print("CSV does not exist")
        all_pauses={}
        for book in os.listdir('../resources'):
            print(book)
            all_lengths.update(getAvgLength("resources/{}".format(book)))
        print("completed calculating sentence lengths successfully")
        with open('../book_sent_lens.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in all_lengths.items():
                writer.writerow([key, value])
        return all_pauses

'''
Find the average sentence length of an already-downloaded txt file"
'''
def getAvgPause(filename):
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
                pauses=",;--—:"
                sents=nltk.sent_tokenize(book_text)
                num_pauses=0.0
                num_sents=len(sents)
                for sentence in sents:
                    words=nltk.word_tokenize(sentence)
                    for word in words:
                        if word in pauses:
                            num_pauses+=1.0
                        else:
                            pass
                print({book_title:num_pauses/num_sents})
                return {book_title:num_pauses/num_sents}
        except:
            print()
            print("Error parsing file {}!".format(filename))
            # sys.exit()
