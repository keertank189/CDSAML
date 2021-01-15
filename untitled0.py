#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:36:26 2018

@author: keertankrishnan
"""

#import pickle as p
import json as j
en_dirname = "/Users/keertankrishnan/Documents/Project Work/CDSAML/Old Laptop Files/CDSAML/news/"
hi_dirname = "/Users/keertankrishnan/Documents/Project Work/CDSAML/Old Laptop Files/CDSAML/news/"
hin=open(hi_dirname+"s8"+"(new)_hindi_training(clean_no_handle).txt","r")
eng=open(en_dirname+"s8"+"(new)_eng_huge_set_clean(no_handle).txt","r")
tagse=open(en_dirname+ "tags_training(en).txt","w")
tagsh=open(hi_dirname+"tags_training(hi).txt","w")

"""Training data files loaded"""
count=0
num_tags_hi=[]     #to hold the lists of numerical tags 0,1,-1 for training tweets
for line in hin:
    num_tags_tweet=[] #holds the tags of 0,-1,1 for each training tweet
    #print(line[0])
    line=line.split(" ")
    #print(line)
    for i in line:
        num_tags_tweet.append(-1)
    count+=1
    num_tags_hi.append(num_tags_tweet)
num_tags_en=[]     #to hold the lists of numerical tags 0,1,-1 for training tweets
for line in eng:
    num_tags_tweet=[] #holds the tags of 0,-1,1 for each training tweet
    #print(line[0])
    line=line.split(" ")
    #print(line)
    for i in line:
        num_tags_tweet.append(1)
    count+=1
    num_tags_en.append(num_tags_tweet)
"""y-output generated"""
tagsh.write(j.dumps(num_tags_hi))
tagse.write(j.dumps(num_tags_en))
"""Tags written to file"""

hin.close()
eng.close()
tagse.close()
tagsh.close()
    


    
