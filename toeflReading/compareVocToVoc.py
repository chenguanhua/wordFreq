from stemming.porter2 import stem
import string
import csv
import re

def output(dict,path):
    with open('tReadingData/'+path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])


with open('tReadingData/1+2+3+4+5+6+7+8+9.csv', 'rb') as voc:
    text = csv.reader(voc)
    words1=[item[0] for item in text]

wordsStemmed1 = [word for word in words1]

counts = {}

for w in wordsStemmed1:
    counts[w] = counts.get(w,0) + 1

with open('tReadingData/10_30.csv', 'rb') as voc:
    text = csv.reader(voc)
    words2=[item[0] for item in text]

wordsStemmed2 = [word for word in words2]

overlap={}

for i in range(len(wordsStemmed2)):
    overlap[wordsStemmed2[i]]=counts.get(wordsStemmed2[i],"none");

output(overlap,'10.csv')