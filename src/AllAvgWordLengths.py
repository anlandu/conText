import os
import AverageWordLength

avgLengths=[]
for book in os.listdir('../resources'):
    print(book)
    avgLengths.append(AverageWordLength.getAvgLength(book[:-4]))
print(avgLengths)
