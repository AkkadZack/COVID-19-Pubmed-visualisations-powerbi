# -*- coding: utf-8 -*-
import re
path="C:\\Users\\MACBOOK AIR\Desktop\\GI3\\projet powerBI\\"
file=open(path+'Abstract.txt',"r",encoding="utf-8")
filer=open(path+'verbs.txt',"r",encoding="utf-8")
# Ouvrir le fichier en lecture seulepubmed-covid19-set.txt
filew1 = open(path+'Title_title.txt', 'w')  # url = fichier.txt
filew2 = open(path+'Abstract_abstract.txt', 'w')
filew3 = open(path+'Abstract_abstract_AND_Title_title.txt', 'w')
i = 0
dict={}
temp=[]
listVerb=['hello','hey']
for line in filer:
    listVerb=line.split(",")
dicTI = {'TI': 1}
dicAB = {'AB': 1}
index=0
stop_words = ["although","already","sa", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "ci", "2020", "2019", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
for line in file:
    dictTI = {'TI': 1}
    dictAB = {'AB': 1}
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
        dicTI[index]=dictTI
        dicAB[index]=dictAB
        index+=1
#for key, value in dictTI.items(): 
#    filew1.write('%s:%s\n' % (key, value))
#for key, value in dictAB.items(): 
#    filew2.write('%s:%s\n' % (key, value))   
dicTI.pop('TI') 
dicAB.pop('AB')     
#print(dicTI)
#print(dicAB)
matrice={}
for index,col in enumerate(dicTI):
    for word in dicTI[index]:
        for ww in dicTI[index]:
            key1=(word,ww)
            key2=(ww,word)
            if key1==key2 :
               continue 
            elif key1 in matrice or key2 in matrice: 
                if key1 in matrice:
                    matrice[key1]=matrice[key1]+1
                elif key2 in matrice:
                    matrice[key2]=matrice[key2]+1
                else :
                    matrice[key1]=matrice[key1]+1
            else:
                matrice[key1]=1
matrice1={}
for index,col in enumerate(dicAB):
    for word in dicAB[index]:
        for ww in dicAB[index]:
            key1=(word,ww)
            key2=(ww,word)
            if key1==key2 :
               continue 
            elif key1 in matrice1 or key2 in matrice1: 
                if key1 in matrice1:
                    matrice1[key1]=matrice1[key1]+1
                elif key2 in matrice1:
                    matrice1[key2]=matrice1[key2]+1
                else :
                    matrice1[key1]=matrice1[key1]+1
            else:
                matrice1[key1]=1
matrice2={}
for index,col in enumerate(dicAB):
    for word in dicAB[index]:
        for ww in dicTI[index]:
            add=0
            key1=(word,ww)
            key2=(ww,word)
            if key1 in matrice:
                add+= matrice[key1]
            elif key1 in matrice1:
                add+= matrice1[key1]
            if key2 in matrice:
                add+= matrice[key2]
            elif key2 in matrice1:
                add+= matrice1[key2]
            if key1==key2:
               continue
            elif key1 in matrice2 or key2 in matrice2:
                if key1 in matrice2:
                    matrice2[key1]=matrice2[key1]+1
                elif key2 in matrice2:
                    matrice2[key2]=matrice2[key2]+1
                else:
                    matrice2[key1]=matrice2[key1]+1
            else:
                matrice2[key1]=add+1
                
for key,value in matrice.items():
    filew1.write(' ,'.join(key))
    filew1.write(':%s\n' % (value))
filew1.close()
for key,value in matrice1.items():
    filew2.write(' ,'.join(key))
    filew2.write(':%s\n' % (value))
filew2.close()
for key,value in matrice2.items() :
    filew3.write(' ,'.join(key))
    filew3.write(':%s\n' % (value))
filew3.close()
print("fin")