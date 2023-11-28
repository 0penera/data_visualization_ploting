import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter


#print(plt.style.available)
plt.style.use('seaborn-notebook')

#using pandas 
data = pd.read_csv(r'C:\Users\bokseon hwang\Documents\code\matplotlib\dev_ser_data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
    
for response in lang_responses:
    language_counter.update(response.split(';'))


#csv reader 활용방법
#with open(r'C:\Users\bokseon hwang\Documents\code\matplotlib\dev_ser_data.csv') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
    
#    language_counter = Counter()
    
#    for row in csv_reader:
#        language_counter.update(row['LanguagesWorkedWith'].split(';'))


languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages, popularity)

languages.reverse()
popularity.reverse()
    
plt.barh(languages, popularity)

plt.title("Most Polular languages")
#plt.ylabel("Programming languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()