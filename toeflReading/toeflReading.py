from stemming.porter2 import stem
import string
import csv
import re

text1 = string.lower(text1)

words1=re.findall(r'\b[a-z]+\b', text1)


wordsStemmed1 = [stem(word) for word in words1]

text2 = string.lower(text2)
words2=re.findall(r'\b[a-z]+\b', text2)
wordsStemmed2 = [stem(word) for word in words2]

counts = {}

for w in wordsStemmed1:
    counts[w] = counts.get(w,0) + 1

overlap={}

for i in range(len(wordsStemmed2)):
    overlap[wordsStemmed2[i]]=counts.get(wordsStemmed2[i],"none");

output(overlap)



