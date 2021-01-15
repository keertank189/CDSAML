#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:04:07 2017

@author: smarty pant
"""
import pickle as p
"""
e_dict=open("/home/pant/Desktop/english/train_data/ngrams/e_dict(handle).bin","rb")
h_dict=open("/home/pant/Desktop/hindi/train_data/ngrams/h_dict(handle).bin","rb")
xe=p.load(e_dict)
xh=p.load(h_dict)
e_dict.close()
h_dict.close()"""
def ngrams(tweets, n):

  output = {}
  for tweet in tweets:
      tweet=tweet.split()
      for i in range(len(tweet)-n+1):
        g = ' '.join(tweet[i:i+n])
        output.setdefault(g, 0)
        output[g] += 1
  return output

hi_in_dir='/home/pant/Desktop/hindi/train_data/'
hi_files=["s8_hindi_training(clean_no_handle).txt"]
#hi_files=["s8_hin_huge_training_data.txt"]

#make new list if you wish to add more n grams to existing files
#en_in_dir='/home/pant/Desktop/english/train_data/'
#en_files=["s8_eng_huge_set_clean.txt"]#(works well for one file at a time)
#en_files=["s8_english.clean","s8_english_clean_my.txt"]

#e_dict=open("/home/pant/Desktop/english/train_data/ngrams/e_dict(handle).bin","wb")
h_dict=open("/home/pant/Desktop/hindi/train_data/ngrams/hindi_dict(clean).bin","wb")
'''
en1g=[]
en2g=[]
en3g=[]
en4g=[]
'''
hi1g=[]
hi2g=[]
hi3g=[]
hi4g=[]
for i in range(1,5):
'''
    for en_file in en_files:
        
        finput=open(en_in_dir+en_file,"r")
        ngram=open(en_in_dir+"/ngrams/"+"s8_en_"+str(i)+"gram(handle).txt","w")
        x=finput.readlines() 
        dictionary=ngrams(x,i)
        if i==1:
            del dictionary["<s>"]
            del dictionary["</s>"]
        for k in dictionary:
            
#            if i==1:
#                if k=="<s>" or k=="</s>":
#                    continue
                
            ngram.write(k+" "+str(dictionary[k])+"\n")
            l=k.split()
            if i==1:
                en1g.append(l)
            elif i==2:
                en2g.append(l)
            elif i==3:
                en3g.append(l)
            else:
                en4g.append(l)
        finput.close()
    ngram.close()
    p.dump(dictionary,e_dict)
'''
    for hi_file in hi_files:
        
        finput=open(hi_in_dir+hi_file,"r")
        ngram=open(hi_in_dir+"/ngrams/"+"s8_hindi_"+str(i)+"gram(clean).txt","w")
        #ngram=open(hi_in_dir+"/ngrams/"+"hi_"+str('1')+"gram.txt","w")
        x=finput.readlines()   
        dictionary=ngrams(x,i)
        if i==1:
            del dictionary["<s>"]
            del dictionary["</s>"]
        for k in dictionary:

            ngram.write(k+" "+str(dictionary[k])+"\n")
            l=k.split()
            if i==1:
                hi1g.append(l)
            elif i==2:
                hi2g.append(l)
            elif i==3:
                hi3g.append(l)
            else:
                hi4g.append(l)
        finput.close()
    ngram.close()
    p.dump(dictionary,h_dict)


hin=open(hi_in_dir+"/ngrams/"+"s8_"+"hindi(clean).bin","wb")
#eng=open(en_in_dir+"/ngrams/"+"s8_"+"eng(handle).bin","wb")

p.dump(hi4g,hin)
p.dump(hi3g,hin)
p.dump(hi2g,hin)
p.dump(hi1g,hin)
'''
p.dump(en4g,eng)
p.dump(en3g,eng)
p.dump(en2g,eng)
p.dump(en1g,eng)'''
"""
print(j.dumps(hi4g))
print(p.dumps(hi3g))
print(p.dumps(hi2g))
print(p.dumps(hi1g))

j.dumps(en4g)
j.dumps(en3g)
j.dumps(en2g)
j.dumps(en1g)
"""
hin.close()
#eng.close()

#e_dict.close()
h_dict.close()

