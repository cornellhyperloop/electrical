#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:40:08 2019

@author: aneesh
"""
import random
import time

for i in range(100):
    f= open("sample_data.txt","a+")
    x = random.randint(20,50)
    f.write(str(i) + ", " + str(x))
    f.write("\n")
    time.sleep(1)
    f.close() 
 
