#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:52:36 2017

@author: keertan
"""

from scipy.stats import describe
f=open("results.txt")
score=[]
for line in f:
    score.append(float(line))
print(describe(score))
    