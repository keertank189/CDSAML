#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 15:58:32 2017

@author: pant
"""

import time
import pickle as p

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

        cmp=lst[mid]
        if ele==cmp:
            return 1
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

hin=open(hi_dirname+"s8_"+"hindi(clean)_fast.bin","rb")
eng=open(en_dirname+"s8_"+"eng_fast.bin","rb")
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
adir ="/home/keertan/Desktop/news/"
afname = "sum score"
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
num_words=0
tw=0
num3=0
begin=time.time()
count=1
for sent in qf:
    if count >6186:
        break
    text=next(qflang_line)
    words = sent.split()
#    print(count," . ",sent)
    wc = len(words)
    sent_score = {en: 0, hi: 0}
    c=0
    for inde,w in enumerate(words):
#        print("word ",inde+1," : ",w)
        if inde==0 or inde==wc-1:
            continue
        word_score = {en: 0, hi: 0}
        index = inde
        for n in range(4,0,-1):
#            print("n=",n)
            if word_score[en]>=n and word_score[hi]>=n:
#                print("discarding redundant computation")
                break
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
                if word_score[en]>=n and word_score[hi]>=n:
#                    print("discarding redundant computation")
                    break
                if search(ele,english[4-n]):        
                    word_score[en] = max(word_score[en], n)
#                    word_score[en] += n
                if search(ele,hindi[4-n]):
                    word_score[hi] = max(word_score[hi], n)
#                    word_score[hi] += n
#                print(en,word_score[en], "\t",hi, word_score[hi])

#        print("final word scores:")    
#        print(en,word_score[en], "\t",hi, word_score[hi])  
        if word_score[en]==word_score[hi] and w!="<s>" and w!="</s>":
            c+=1
        sent_score[en] = sent_score[en] + pow(word_score[en],2)
        sent_score[hi] = sent_score[hi] + pow(word_score[hi],2)
#        sent_score[en] = sent_score[en] + word_score[en]
#        sent_score[hi] = sent_score[hi] + word_score[hi]
#        print("sent score :")
#        print(en,sent_score[en], "\t",hi, sent_score[hi])

    num_words+=c
    if c<(wc-2)/6:
        tw+=1
#    print("\n*********\n")
    if sent_score[hi]>sent_score[en]:
#    if(sent_score[hi]>sent_score[en]):
        tag="<class>2</class>"
    elif sent_score[hi]<sent_score[en]:
#    elif (sent_score[hi]<sent_score[en]):
        tag="<class>1</class>"
    else:
        num3+=1
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
end=time.time()
pred_time=end-begin
print("prediction time: ",pred_time)
af.close()
qf_lang.close()
qf.close()

print(c)