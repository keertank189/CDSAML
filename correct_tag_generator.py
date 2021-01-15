 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:41:18 2017

@author: keertan
"""
#This code generates 1 for english, -1 for hindi and 0 for undefined
import json
tagged_dir="/home/keertan/Documents/CDSAML/news/"
tagged_file="twitter_data_pure_mixed.txt"
tagged_list_dir="/home/keertan/Documents/CDSAML/news/"
tagged_list_file="twitter_data_tagged.txt"
tag_fp=open(tagged_dir+tagged_file,"r")
tag_list=open(tagged_list_dir+tagged_list_file,"w")
for i in range(0,0):
    tag_fp.readline()
count=1
list_scores=[]
for line in tag_fp:
    if(count>1000):
        break
    else:
        words=line.split()
        l=[]
        flag=0
        for word in words:
            if word in ['<s>','</s>']:
                continue
            if (word[:3]=='<e>'):
                l.append(1)
                flag=1
            elif(word[:3]=='<h>'):
                l.append(-1)
                flag=-1
            elif(flag==1):
                l.append(1)
            elif(flag==-1):
                l.append(-1)
            elif(word[:5]=='<und>'):
                l.append(0)
                flag=0
            elif(flag==0):
                l.append(0)
        list_scores.append(l)
    count+=1
json.dump(list_scores,tag_list)
tag_list.close()
tag_fp.close()
print(list_scores)