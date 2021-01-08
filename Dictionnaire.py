# -*- coding: utf-8 -*-
import re
path='D:\\utilisateur\\Documents\\Projet PowerBI\\'
file=open(path+'Abstract.txt',"r")
filer=open(path+'verb.txt',"r")
# Ouvrir le fichier en lecture seulepubmed-covid19-set.txt
filew1 = open(path+'Title_Keys.txt', 'w')  # url = fichier.txt
filew2 = open(path+'Abstract_Keys.txt', 'w')
i = 0
dict={}
temp=[]
listVerb=['hello','hey']
for line in filer:
    listVerb=line.split(",")
dictTI = {'TI': 1}
dictAB = {'AB': 1}
stop_words = ["although","already","a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
for line in file:
    temp= line.split('|')
    if len(temp)>2:
        TI0 = temp[1]
        AB0= temp[2]
        PMID0=temp[0]
        PMID1=PMID0.split('-',1)
        TI1=TI0.split('-',1)
        AB1=AB0.split('-',1)
        TI=TI1[1]
        TI=TI.split(" ")
        AB=AB1[1]
        AB=AB.split(" ")
        PMID=PMID1[1]
        PMID=PMID.strip()
        for word in TI:
            word=word.strip()
            filter(str.isalnum,word)
            #word=word.lower()
            word=re.sub(r"[^a-z0-9-]","",word.lower())
            #print(word)
            if dictTI.__contains__(word) and len(word)>1 and word not in stop_words and word not in listVerb:
                 dictTI[word]=dictTI[word] + 1
            elif  len(word)>1 and word not in stop_words and word not in listVerb:
                 dictTI[word]=1
        for word in AB:
            word=word.strip()
            filter(str.isalnum,word)
            word=re.sub(r"[^a-z0-9-]","",word.lower())
            #print(word)
            if dictAB.__contains__(word) and len(word)>1 and word not in stop_words and word not in listVerb:
                 dictAB[word]=dictAB[word] + 1
            elif  len(word)>1 and word not in stop_words and word not in listVerb:
                 dictAB[word]=1
        #print(dictAB)
dictTI.pop('TI')
dictAB.pop('AB')
for key, value in dictTI.items(): 
    filew1.write('%s:%s\n' % (key, value))
for key, value in dictAB.items(): 
    filew2.write('%s:%s\n' % (key, value))        
print("fin")
