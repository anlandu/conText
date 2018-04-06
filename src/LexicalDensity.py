'''
Methods to generate average sentence length of a file, create file containing
average sent lengths of all files in a directory, and given a Project Gutenberg
URL, return the text with the closest average sentence length'''
import string
import requests
import nltk
nltk.download('punkt')
nltk.download('stopwords')
# from nltk import RegexpTokenizer
from nltk.corpus import stopwords
import sys
import os
import csv

'''
Given a Project Gutenberg URL, get the book (out of top 100 on Project Gutenberg)
with the closest average sentence length
'''
def getClosestDens(input):
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
    user_book_lex_dens=getAvgDens("userBook.txt").get("User Chosen Text")
    closest_diff=9999.0
    closest_book="None"
    all_book_dens=getAllDens()
    for title, avg_lex_dens in all_book_dens.items():
        curr_diff=abs(user_book_lex_dens-float(avg_lex_dens))
        if curr_diff < closest_diff:
            closest_book=title
            closest_diff=curr_diff
    return "Book with closest average sentence length: " + closest_book

'''
Read or, if non-existent, create a CSV of the average sentence lengths of all of the
top 100 books
'''
def getAllDens():
    if os.path.exists("../book_lexical_densities.csv"):
        print("CSV exists")
        with open('../book_lexical_densities.csv', 'r', newline="\n", encoding="utf-8", errors="ignore") as csv_file:
            reader = csv.reader(csv_file)
            all_dens=dict(reader)
        return all_dens

    else:
        print("CSV does not exist")
        all_dens={}
        for book in os.listdir('../resources'):
            print(book)
            all_dens.update(getAvgDens("resources/{}".format(book)))
        print("completed calculating lexical densities successfully")
        with open('../book_lexical_densities.csv', 'w+', encoding="utf-8", errors="ignore") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in all_dens.items():
                writer.writerow([key, value])
        return all_dens

'''
Find the average sentence length of an already-downloaded txt file"
'''
def getAvgDens(filename):
        # try:
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
            punctuation=string.punctuation+")’(,�--|~"
            words=nltk.word_tokenize(book_text)
            num_function_words=0.0
            num_stopwords=0.0
            stopset=set(stopwords.words('english'))
            for word in words:
                if word in punctuation:
                    pass
                elif word in stopset:
                    num_stopwords+=1.0
                else:
                    num_function_words+=1.0
            total_words=num_function_words+num_stopwords
            print({book_title:num_function_words/total_words})
            return {book_title:num_function_words/total_words}
