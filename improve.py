#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 11:12:10 2017

@author: pant
"""

import pickle as p
from operator import itemgetter

hi_dirname = "/home/pant/Desktop/hindi/train_data/ngrams/"
hin=open(hi_dirname+"s8_"+"hindi(clean).bin","rb")
new_hin=open(hi_dirname+"s8_"+"hindi(clean)_fast.bin","wb")

hi=p.load(hin)
print(4)
new=sorted(hi,key=itemgetter(0,1,2,3))
p.dump(new,new_hin)

hi=p.load(hin)
print(3)
new=sorted(hi,key=itemgetter(0,1,2))
p.dump(new,new_hin)

hi=p.load(hin)
print(2)
new=sorted(hi,key=itemgetter(0,1))
p.dump(new,new_hin) 

hi=p.load(hin)
print(1)
new=sorted(hi,key=itemgetter(0))
p.dump(new,new_hin) 
hin.close()
new_hin.close()     
'''
en_dirname = "/home/pant/Desktop/english/train_data/ngrams/"
eng=open(en_dirname+"s8_"+"eng(handle).bin","rb")
new_eng=open(en_dirname+"s8_"+"eng(handle)_fast.bin","wb")

en=p.load(eng)
print(4)
new=sorted(en,key=itemgetter(0,1,2,3))
p.dump(new,new_eng)

en=p.load(eng)
print(3)
new=sorted(en,key=itemgetter(0,1,2))
p.dump(new,new_eng)

en=p.load(eng)
print(2)
new=sorted(en,key=itemgetter(0,1))
p.dump(new,new_eng) 

en=p.load(eng)
print(1)
new=sorted(en,key=itemgetter(0))
p.dump(new,new_eng) 

eng.close()
new_eng.close()
'''
"""
new_hin=open(hi_dirname+"s8_"+"hin_fast.bin","rb")  
x=p.load(new_hin)
print(x[:15])
new_hin.close()   """     