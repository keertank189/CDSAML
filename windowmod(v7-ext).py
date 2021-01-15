#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:34:26 2017

@author: pant
"""


import time
import pickle as p
import json as j

def compare(ele,cmp):
    l=sorted([ele,cmp])
    if l[0]==ele:
        return 0
    else:
        return 1
def search(ele,lst):
    l=0
    u=len(lst)-1
    while l<=u:
        mid=int((l+u)/2)
        cmp=lst[mid][:-1]
        freq=lst[mid][-1]
        if ele==cmp:
            return freq
            break
        elif compare(ele,cmp):
            l=mid+1
        else:
            u=mid-1
    else:
        return 0
    
from enchant import Dict
d=Dict("en_GB")
start=time.time()
en_dirname = "/home/keertan/Desktop/news/"
hi_dirname = "/home/keertan/Desktop/news/"
hindi=[]
english=[]

hin=open(hi_dirname+"s8_"+"hindi(clean_no_handle_withfreq)_fast.bin","rb")
eng=open(en_dirname+"s8_"+"eng(withfreq)_fast.bin","rb")
for k in range(4,0,-1):
    hindi.append(p.load(hin))
    english.append(p.load(eng))

end_train=time.time()
train_time=end_train-start
print("training time: ",train_time)

hin.close()
eng.close()
#end of training


st=time.time()
qdir = "/home/keertan/Desktop/news/"

qfname = "s8_completely_new_test_no_handle.txt"
qflangname="completely_new_test_no_handle.txt"


"""
qfname = "s8_und_test"
qflangname="und_test"
"""
qf = open(qdir+qfname)
qf_lang=open(qdir+qflangname)
adir = "/home/keertan/Desktop/news/"
afname = "wmod(v7)(try2).txt"
af = open(adir+afname, "w")

preddir="/home/keertan/Desktop/news/"
predname="word_tagged_predicted(v7)"
pred=open(preddir+predname,"w")

def generator():
    for line in qf_lang:
        yield line
en="en"
hi="hi"
un="un"       
qflang_line=generator()

for i in range(0,0):
    qf.readline()
    next(qflang_line)
    
print("finished iterating")
sto=time.time()
print("in :",sto-st)

c=0
num3=0 
begin=time.time()
count=1
w_changes=[]
for sent in qf:
    if count >1000:
        break
    text=next(qflang_line)
    ltext=text.split()
    words = sent.split()
#    print(count," . ",sent)
    wc = len(words)
    sent_score = {en: 0, hi: 0}
    wordln={en : 0, hi : 0, un : 0}
    change=[]
    for inde,w in enumerate(words):
#        print("word ",inde+1," : ",w)
        if inde==0 or inde==wc-1:
            continue
        word_score = {en: 0, hi: 0}
        index = inde
        for n in range(4,0,-1):
#            print("n=",n)
#            if word_score[en]>=n and word_score[hi]>=n:
#                print("discarding redundant computation")
#                break
            ngrams_list = []
            start = 0
            end = wc-1
            if(index-n+1>start):
                start = index-n+1
            if(end>index+n-1):
                end = index+n-1
            i = start
            while (i+n-1<=end):
                ngrams_list.append(words[i:i+n])
                i = i+1
#            print(ngrams_list)
#            print("training data sample: ",english[4-n][1:6])
            for ele in ngrams_list:

                freq=search(ele,english[4-n])
                if freq:

#                    word_score[en] = max(word_score[en], n*freq)
                    word_score[en] += (n**15)*(freq**0.1)
                freq=search(ele,hindi[4-n])    
                if freq: 
#                    word_score[hi] = max(word_score[hi], n*freq)
                    word_score[hi] += (n**15)*(freq**0.1)
#                print(en,word_score[en], "\t",hi, word_score[hi])

#            print("final word scores:")    
#            print(en,word_score[en], "\t",hi, word_score[hi]) 
        if word_score[en]==word_score[hi]:
            c+=1
            wordln[un]+=1
            change.append(0)
#            print(ltext[inde],"und")
        elif word_score[en]>word_score[hi]:
            wordln[en]+=1
            change.append(1)
#            print(ltext[inde],"en")
        else:
            wordln[hi]+=1
            change.append(-1)
#            print(ltext[inde],"hi")
#        sent_score[en] = sent_score[en] + pow(word_score[en],2)
#        sent_score[hi] = sent_score[hi] + pow(word_score[hi],2)
#        sent_score[en] = sent_score[en] + word_score[en]
#        sent_score[hi] = sent_score[hi] + word_score[hi]
#            print("sent score :")
#            print(en,sent_score[en], "\t",hi, sent_score[hi])

    
#    print("\n*********\n")
    if wordln[en]>wordln[hi]:
        tag="<class>1</class>"
    elif wordln[en]<wordln[hi]:
        tag="<class>2</class>"
        
#    if(sent_score[hi]>sent_score[en]):
#        tag="<class>2</class>"
#    elif (sent_score[hi]<sent_score[en]):
#        tag="<class>1</class>"
    else:
        num3+=1
        eng="abcdefghijklmnopqrstuvwxyz"
        l=text.split()
        n=[]
        for e in l:
            f=0
            for i in e:
                if i not in eng:
                    f=1
                    break
            if f==1:
                continue
            n.append(e)
        wc=len(n)
        if wc<3:
            tag="<class>3</class>"
        else:
            ct=0
            for e in n:
                if d.check(e):
                    ct+=1
            if ct>wc/2:
                tag="<class>1</class>"
            else:
                tag="<class>2</class>"

    w_changes.append(change)   
    af.write(text+" "+tag+"\n")
#    print(count)
    count+=1
    af.flush()
end=time.time()
pred_time=end-begin
print("prediction time: ",pred_time)
af.close()
qf_lang.close()
qf.close()

print( "num equal:",c)
print("num class 3",num3)
print("num tweets",len(w_changes))
j.dump(w_changes,pred)
pred.close()