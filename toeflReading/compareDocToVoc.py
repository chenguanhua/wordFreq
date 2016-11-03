from stemming.porter2 import stem
import string
import csv
import re

def output(dict,path):
    with open('tReadingResults/'+path, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dict.items():
            writer.writerow([key, value])


with open('tReadingData/6_34.txt', 'r') as myfile:
    text1=myfile.read().replace('\n', '')

text1 = string.lower(text1)

words1=re.findall(r'\b[a-z]+\b', text1)

wordsStemmed1 = [stem(word) for word in words1]

counts = {}

for w in wordsStemmed1:
    counts[w] = counts.get(w,0) + 1

with open('tReadingData/21-30 voc.csv', 'rb') as voc:
    text = csv.reader(voc)
    words2=[item[0] for item in text]

wordsStemmed2 = [word for word in words2]

overlap={}

for i in range(len(wordsStemmed2)):
    overlap[wordsStemmed2[i]]=counts.get(wordsStemmed2[i],"none");

print overlap
print len(counts.keys())
print wordsStemmed1
print len(words1)
print len(wordsStemmed1)
print len(wordsStemmed2)

num=0
for word in counts.keys():
    if word in wordsStemmed2:
        num=num+1

print num*1.0/len(counts.keys())