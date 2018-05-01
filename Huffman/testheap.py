# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 14:58:36 2018

@author: hagar
"""

import heapq

import symbol as s



ar=s.Symbol('a',5,0.5)
arr=[ar]
print(arr[0].value)

import encoder
r=encoder.Encoder('t1.tsv')
# initializing list
#li = [5, 7, 9, 1, 3]
li=r.symbols
 
# using heapify to convert list into heap
heapq.heapify(li)
 
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
for i in li:
    print(i)
#print(li[0])
print(len(li))
 
# using heappush() to push elements into heap
# pushes 4
#heapq.heappush(li,4)
 
## printing modified heap
#print ("The modified heap after push is : ",end="")
#print (list(li))
# 
## using heappop() to pop smallest element
#print ("The popped and smallest element is : ",end="")
#print (heapq.heappop(li))
