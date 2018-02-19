
'''
IN PROGRESS
Creates a table of the average word length of the top 100 books on Project Gutenberg
'''
import os
import AverageWordLength

avgLengths={}
for book in os.listdir('../resources'):
    if book != "userInputtedText":
        print(book)
        avgLengths.update(AverageWordLength.getAvgLength(book))
print(avgLengths)
