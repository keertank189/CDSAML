#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:06:50 2017

@author: keertan
"""
qflangname="completely_new_test_no_handle.txt"
qdir = "/home/keertan/Desktop/news/"
qf_lang=open(qdir+qflangname)
adir ="/home/keertan/Desktop/news/"
afname = "exp"
af = open(adir+afname, "w")
count=0
for text in qf_lang:
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
qf_lang.close()
af.close()