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
import os
import csv

def getClosestLength(input):
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
    user_book_word_len=getAvgLength("userBook.txt").get("User Chosen Text")
    closest_diff=9999.0
    closest_book="None"
    all_book_lengths=getAllLengths()
    # print(all_book_lengths)
    for title, avg_len in all_book_lengths.items():
        curr_diff=abs(user_book_word_len-float(avg_len))
        if curr_diff < closest_diff:
            closest_book=title
            closest_diff=curr_diff
    return closest_book

def getAllLengths():
    print("madeit")
    if os.path.exists("../book_word_lens.csv"):
        print("CSV exists")
        with open('../book_word_lens.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            all_lengths=dict(reader)
        return all_lengths

    else:
        print("CSV does not exist")
        all_lengths={}
        for book in os.listdir('../resources'):
            print(book)
            all_lengths.update(getAvgLength("resources/{}".format(book)))
        print("completed calculating word lengths successfully")
        with open('../book_word_lens.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            print("opened csv successfully")
            writer = csv.writer(csv_file)
            print(all_lengths)
            for key, value in allLengths.items():
                print(key)
                writer.writerow([key, value])
        return all_lengths


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
