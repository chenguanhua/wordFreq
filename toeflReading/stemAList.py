from stemming.porter2 import stem
import string
import csv
import re

def output(list,path):
    with open('tReadingData/'+path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for item in list:
            writer.writerow([item])


with open('tReadingData/wym.csv', 'rb') as voc:
    text = csv.reader(voc)
    words1=[item[0] for item in text]

wordsStemmed1 = [stem(word) for word in words1]

output(wordsStemmed1,'wym_stemmed.csv')