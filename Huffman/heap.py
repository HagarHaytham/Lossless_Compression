# -*- coding: utf-8 -*-
"""
Created on Tue May  1 15:07:37 2018

@author: hagar
"""

import symbol
import heapq 
#class node:
#    def __init__(self,symb):
#        self.symb=symb
#        self.left=self.right=None#dah el null , mafeesh pointers ,let's just try
#        
#struct compare {
# 
#    bool operator()(MinHeapNode* l, MinHeapNode* r)
# 
#    {
#        return (l->freq > r->freq);
#    }
#};
# 

def printCodes(root,code):
    if(root==None):
        return     
    if(root.symb.value !='a'):
        #inset in a dict
        print(root.symb.value+" "+code)
    printCodes(root.left,code+"0")
    printCodes(root.right,code+"1")

def HuffmanCodes(nodearr):
    heapq.heapify(nodearr)
    while (len(nodearr !=1)):
        l=heapq.heappop(nodearr)
        r=heapq.heappop(nodearr)
        data=symbol.Symbol('a',l.frequency+r.frequency,l.probability+r.probability)
        top=symbol.Symbol(data)
        top.left=l
        top.right=r
        heapq.heappush(nodearr,top)
    printCodes(nodearr[0],"")
    