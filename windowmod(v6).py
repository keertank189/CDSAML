#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:34:26 2017

@author: pant
"""


import time
import pickle as p
import json
#l1=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1]]
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
en_dirname = "/home/keertan/Documents/CDSAML/news/"
hi_dirname = "/home/keertan/Documents/CDSAML/news/"
wtagged_predicted_dir="/home/keertan/Documents/CDSAML/news/"
wtagged_predicted_fname="word_tagged_predicted(v6)(test).txt"
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
qdir = "/home/keertan/Documents/CDSAML/news/"

qfname = "s8_completely_new_test_no_handle.txt"
qflangname="completely_new_test_no_handle.txt"


"""
qfname = "s8_und_test"
qflangname="und_test"
"""
qf = open(qdir+qfname)
qf_lang=open(qdir+qflangname)
adir = "/home/keertan/Documents/CDSAML/news/"
afname = "new test1"
af = open(adir+afname, "w")

def generator():
    for line in qf_lang:
        yield line
en="en"
hi="hi"       
qflang_line=generator()

for i in range(0,0):
    qf.readline()
    next(qflang_line)
    
print("finished iterating")
sto=time.time()
print("in :",sto-st)

c=0 
begin=time.time()
count=1
w_changes=[]
tagged_predicted=open(wtagged_predicted_dir+wtagged_predicted_fname,"w")
for sent in qf:
    if count >6186:
        break
    text=next(qflang_line)
    words = sent.split()
    #print("lenght of words:",len(words))
    change=[]
#    print(count," . ",sent)
    wc = len(words)
    sent_score = {en: 0, hi: 0}
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

                    word_score[en] = max(word_score[en], n*freq)
#                   word_score[en] += n*freq
                freq=search(ele,hindi[4-n])    
                if freq: 
                    word_score[hi] = max(word_score[hi], n*freq)
#                    word_score[hi] += n*freq
        if(word_score[hi]>word_score[en]):
                    change.append(-1)
        elif(word_score[hi]==word_score[en]):
                    change.append(0)
        else:
                    change.append(1)
            
              
                    
#                print(en,word_score[en], "\t",hi, word_score[hi])

#            print("final word scores:")    
#            print(en,word_score[en], "\t",hi, word_score[hi]) 
        if word_score[en]==word_score[hi] and w!="<s>" and w!="</s>":
            c+=1
        sent_score[en] = sent_score[en] + pow(word_score[en],2)
        sent_score[hi] = sent_score[hi] + pow(word_score[hi],2)
#        sent_score[en] = sent_score[en] + word_score[en]
#        sent_score[hi] = sent_score[hi] + word_score[hi]
#            print("sent score :")
#            print(en,sent_score[en], "\t",hi, sent_score[hi])
    w_changes.append(change)
    #print(len(change))
    
    
    
    #print(len(change))
#    print("\n*********\n")
    if(sent_score[hi]>sent_score[en]):
        tag="<class>2</class>"
    elif (sent_score[hi]<sent_score[en]):
        tag="<class>1</class>"
    else:
#        af.write(text+" <class>3</class>\n")  #remember to find and replace cannot determine with 3
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

    af.write(text+" "+tag+"\n")
    print(count)
    count+=1
    af.flush()
#print(w_changes)
json.dump(w_changes,tagged_predicted)
tagged_predicted.close()
end=time.time()
pred_time=end-begin
print("prediction time: ",pred_time)
af.close()
qf_lang.close()
qf.close()

print(c)