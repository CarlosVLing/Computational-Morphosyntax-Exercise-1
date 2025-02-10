# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:37:11 2025

@author: carlv
"""
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import spacy

# Variables to store the texts in both Spanish and English
esp = ""
eng = ""

# Read and concatenate the spanish files, stored at the ESP directory
txt_files = Path("./ESP/").glob("*.txt")
for txt in txt_files:
    with open(txt, encoding='utf-8') as f:
        esp += f.read()

# Read and concatenate the english files, stored at the ENG directory
txt_files = Path("./ENG/").glob("*.txt")
for txt in txt_files:
    with open(txt, encoding='utf-8') as f:
        eng += f.read()

# Create spacy nlp objects
nlp = spacy.blank("en")
doc = nlp(eng)
nlp2 = spacy.blank("es")
doc2 = nlp2(esp)

#Extract all tokens that are not URLS, emails or punctuation 
eng_words = [token.text for token in doc if not (token.is_punct or token.like_email or token.like_url or token.like_num)]
esp_words = [token.text for token in doc2 if not (token.is_punct or token.like_email or token.like_url or token.like_num)]

#Extra cleaning for english words with the format "------------USAGE"
for word in eng_words:
    if len (word)>20:
        if "-----" in word:
            eng_words.remove(word)

#Get word lengths and count their frequences
length_eng=[len(word) for word in eng_words]
length_esp=[len(word) for word in esp_words]
total_esp=Counter (length_esp)
total_eng=Counter (length_eng)


#Plot the lengths
df = pd.DataFrame(total_eng.items(), columns=['Length', 'Freq'])
plt.figure(figsize=(10, 5))
sns.barplot(x='Length', y='Freq', data=df)
plt.xlabel('Length')
plt.ylabel('Freq')
plt.title('Frequencies ENG')
plt.savefig('freq_eng.png', dpi=300)
plt.show()

df = pd.DataFrame(total_esp.items(), columns=['Length', 'Freq'])
plt.figure(figsize=(10, 5))
sns.barplot(x='Length', y='Freq', data=df)
plt.xlabel('Length')
plt.ylabel('Freq')
plt.title('Frequencies ESP')
plt.savefig('freq_esp.png', dpi=300)
plt.show()