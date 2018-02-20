
'''
Creates a table of the average word length of the top 100 books on Project Gutenberg
'''
import os
import AverageWordLength

avgLengths={}
for book in os.listdir('../resources'):
    print(book)
    avgLengths.update("resources/{}".format(AverageWordLength.getAvgLength(book)))
print(avgLengths)
