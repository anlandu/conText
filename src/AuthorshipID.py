import json
import string
import requests
from nltk import RegexpTokenizer
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import os
import csv
from bs4 import BeautifulSoup
import re
from collections import Counter
import statistics as stats
import pandas as pd
from sklearn import preprocessing
import numpy as np
'''
TODO: clean up documentation, separate analysis into separate class (where do we
draw the line between data collection and analysis?), figure out whether more
extensive use of PCA would be actually useful, find a time-efficient way of using
tf-idf for single book comparison against a corpus
'''
class AuthID:
    def load_text( self, url):
        if url[-4:]!=".txt":
            print("Invalid URL: Not a .txt file")
        try:
            res=requests.get(url)
            with open("../userChosenText.txt", 'w+', encoding='utf-8', errors="ignore") as f:
                f.write("USER CHOSEN BOOK~~~"+res.text)
        except:
            print("Error retrieving book")

    def write_stats_csv(self):
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
                        all_data.update(self.get_stats(os.path.join(path, name)))
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

    def get_stats(self, filename):
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
            try:
                author=filename[filename.index("resources\\")+10:filename.rfind("\\")]
            except:
                author="Unknown"
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
            all_nums={}
            pos_counter=Counter(diff_pos)
            all_nums.update(pos_counter)
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

    def get_diffs(self):
        #get user-chosen book stats
        user_stats=self.get_stats("../userChosenText.txt").get('USER CHOSEN BOOK')
        print(user_stats)
        if not os.path.exists("../book_stats.csv"):
            write_stats_csv()
        else:
            with open('../book_stats.csv', 'r', encoding="utf-8", newline="", errors="ignore") as csv_read:
                with open('../book_diffs.csv', 'w+', encoding='utf-8', newline='', errors='ignore') as csv_write:
                    reader=csv.DictReader(csv_read)
                    authors_dict={}
                    diff_fields=['author', 'average word length (# chars)', 'average sentence length (# words)', 'type-token ratio', 'lexical density', 'percent nouns', 'percent prepositions', 'percent pronouns']
                    writer = csv.writer(csv_write)
                    writer.writerow(diff_fields)
                    for row in reader:
                        #calculate difference between user book and stored book
                        #for each metric
                        u_words=int(user_stats.get('words'))
                        u_chars=int(user_stats.get('chars'))
                        u_sents=int(user_stats.get('sentences'))
                        u_uwords=int(user_stats.get('unique words'))
                        u_cwords=int(user_stats.get('content words'))
                        u_fwords=int(user_stats.get('function words'))
                        u_nouns=int(user_stats.get('NN'))
                        u_preps=int(user_stats.get('IN'))
                        u_pronouns=int(user_stats.get('PRP'))
                        r_words=int(row.get('words'))
                        r_chars=int(row.get('chars'))
                        r_sents=int(row.get('sentences'))
                        r_uwords=int(row.get('unique words'))
                        r_cwords=int(row.get('content words'))
                        r_fwords=int(row.get('function words'))
                        r_nouns=int(row.get('NN'))
                        r_preps=int(row.get('IN'))
                        r_pronouns=int(row.get('PRP'))
                        avg_word=abs(r_words/r_chars-u_words/u_chars)
                        avg_sent=abs(r_sents/r_words-u_sents/u_words)
                        ttr=abs(r_uwords/r_words-u_uwords/u_words)
                        lex_dens=abs(r_cwords/r_fwords-u_cwords/u_fwords)
                        percent_nouns=abs(r_nouns/r_words-u_nouns/u_words)
                        percent_preps=abs(r_preps/r_words-u_preps/u_words)
                        percent_pronouns=abs(r_pronouns/r_words-u_pronouns/u_words)
                        #create array of each book's closeness to user chosen text
                        if authors_dict.get(row.get('author'))==None:
                            diffs={'avg_word':[avg_word], 'avg_sent':[avg_sent],
                                    'ttr':[ttr], 'lex_dens':[lex_dens],
                                    'percent_nouns':[percent_nouns], 'percent_preps':[percent_preps],
                                    'percent_pronouns':[percent_pronouns]}
                            authors_dict.update({row.get('author'):diffs})
                        else:
                            author_row=authors_dict.get(row.get('author'))
                            author_row.get('avg_word').append(avg_word)
                            author_row.get('avg_sent').append(avg_sent)
                            author_row.get('ttr').append(ttr)
                            author_row.get('lex_dens').append(lex_dens)
                            author_row.get('percent_nouns').append(percent_nouns)
                            author_row.get('percent_preps').append(percent_preps)
                            author_row.get('percent_pronouns').append(percent_pronouns)
                    #get each the median closeness among an author's books
                    for author in authors_dict:
                        author_row=authors_dict.get(author)
                        author_medians={'author':author,
                        'average word length (# chars)':stats.median(author_row.get('avg_word')),
                        'average sentence length (# words)':stats.median(author_row.get('avg_sent')),
                        'type-token ratio':stats.median(author_row.get('ttr')),
                        'lexical density':stats.median(author_row.get('lex_dens')),
                        'percent nouns':stats.median(author_row.get('percent_nouns')),
                        'percent prepositions':stats.median(author_row.get('percent_preps')),
                        'percent pronouns':stats.median(author_row.get('percent_pronouns'))
                        }
                        #write to csv
                        wdict=csv.DictWriter(csv_write,diff_fields,extrasaction='ignore')
                        wdict.writerow(author_medians)

    def find_closest_auth(self):
        #define metrics to be normalized and taken into account
        metrics = ['average word length (# chars)', 'average sentence length (# words)', 'type-token ratio', 'lexical density', 'percent nouns', 'percent prepositions', 'percent pronouns']
        authors_df=(pd.read_csv('../book_diffs.csv'))
        #normalize metrics
        authors_df[metrics] = authors_df[metrics].apply(lambda x: (x - x.min()) / (x.max() - x.min()))
        #find sum of squares
        authors_df['sum of squares']=np.sum(np.square(authors_df[metrics]), axis=1)
        authors_df.to_csv('../book_diffs_normalized.csv', sep=',', mode='w+')
        return authors_df.nsmallest(10, 'sum of squares')
