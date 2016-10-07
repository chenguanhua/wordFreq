from stemming.porter2 import stem
import string
import csv
import re

def output(dict,path):
    with open('tReadingData/'+path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])


with open('tReadingData/8_33.txt', 'r') as myfile:
    text1=myfile.read().replace('\n', '')

text1 = string.lower(text1)

words1=re.findall(r'\b[a-z]+\b', text1)

wordsStemmed1 = [stem(word) for word in words1]

counts = {}

for w in wordsStemmed1:
    counts[w] = counts.get(w,0) + 1

output(counts,'8_33.csv')



