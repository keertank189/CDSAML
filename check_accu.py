#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:41:30 2017

@author: pant
"""
#This code checks for the word tagging
tagged=open("/home/keertan/Documents/CDSAML/news/new test1","r")
res=open("/home/keertan/Documents/CDSAML/news/word_tagged_predicted(v6)(test).txt","r")
c=0
TP="TP"
FP="FP"
FN="FN"
prec="precision"
rec="recall"
F1="F1"
c1='<class>1</class>'
c2='<class>2</class>'
c3='<class>3</class>'
ce=0
ch=0
c3e=0
c3h=0
new_c=0
eng={TP:0.0,FP:0.0,FN:0.0,prec:0.0,rec:0.0,F1:0.0}
hi={TP:0.0,FP:0.0,FN:0.0,prec:0.0,rec:0.0,F1:0.0}

for i in range(0,0):
    tagged.readline()
    res.readline()
    res.readline()

  
for i in range(1,65):
    lin=tagged.readline()
    cls=lin.split()[-1]
    print(cls)
    line=res.readline()
    line=res.readline()
    cmp=line.strip()
    
    if cls==c1:
        ce+=1
        if cmp==c2:
            eng[FN]+=1
            hi[FP]+=1
        elif cmp==c1:
            eng[TP]+=1
        elif cmp==c3:
#            print(lin)
#            eng[FN]+=1
            c3e+=1
        
      
    else:
        if i in range(1714,3901):
            new_c+=1
        ch+=1
        if cmp==c2:
            hi[TP]+=1
        elif cmp==c1:
            hi[FN]+=1
            eng[FP]+=1
        elif cmp==c3:
#            print(lin)
#            hi[FN]+=1
            c3h+=1
"""
of=open("/home/pant/Desktop/out_put_window/und","r")
for i in range(1,6187):
    lin=tagged.readline()
    cls=lin.split()[-1]
    line=res.readline()
    line=res.readline()
    cmp=line.strip()
    if cmp!=c3:
        continue
    c+=1
    print(c,lin)
    print(of.readline())
    cmp=of.readline().strip()
    if cls==c1:
        ce+=1
        if cmp==c2:
            eng[FN]+=1
            hi[FP]+=1
        elif cmp==c1:
            eng[TP]+=1
        elif cmp==c3:
#            print(lin)
#            eng[FN]+=1
            c3e+=1
        
      
    else:
        if i in range(1714,3901):
            new_c+=1
        ch+=1
        if cmp==c2:
            hi[TP]+=1
        elif cmp==c1:
            hi[FN]+=1
            eng[FP]+=1
        elif cmp==c3:
#            hi[FN]+=1
            c3h+=1 
"""
eng[prec]=eng[TP]/(eng[TP]+eng[FP])
#eng[rec]=eng[TP]/(eng[TP]+eng[FN])
eng[rec]=eng[TP]/ce
eng[F1]=2*eng[prec]*eng[rec]/(eng[prec]+eng[rec])
hi[prec]=hi[TP]/(hi[TP]+hi[FP])
#hi[rec]=hi[TP]/(hi[TP]+hi[FN])
hi[rec]=hi[TP]/ch
hi[F1]=2*hi[prec]*hi[rec]/(hi[prec]+hi[rec])

print("Precision:   When it predicts yes, how often is it correct?")
print("Recall   :   When it's actually yes, how often does it predict yes")
print("F1:      :   This is a weighted average of the true positive rate (recall) and precision")
print("    %8s %8s %8s"%(prec,rec,F1))

print(" eng %8.3f %8.3f %8.3f"%(eng[prec],eng[rec],eng[F1]))
print(" hin %8.3f %8.3f %8.3f"%(hi[prec],hi[rec],hi[F1]))
print("\n")
print("%8s %16s"%("actual","predicted"))
print("%8s %8s %8s %8s"%(" ","english","hindi","und"))
print("%8s %8d %8d %8d"%("english",eng[TP],eng[FN],c3e))
print("%8s %8d %8d %8d"%("hindi",hi[FN],hi[TP],c3h))
tagged.close()
res.close()
print(new_c)

    