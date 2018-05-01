# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:35 2018

@author: hagar
"""
import symbol
import heapq

def printCodes(map1,root,code):
    if(root==None):
        return     
    if(root.value !='a'):
        #insert in a dict
        map1[root.value]=code
        #print(root.value+" "+code)
    printCodes(map1,root.left,code+"0")
    printCodes(map1,root.right,code+"1")

class Huffman:
    def __init__(self):
        print('hufmman constructor')
        self.map={}
        pass
    
    
    def HuffmanCodes(self,arr):
        print('huffman hufman codes')
        self.symbarr=arr
        heapq.heapify(self.symbarr)
        while (len(self.symbarr) !=1):
            #get the two smallest symbols' frequencies
            l=heapq.heappop(self.symbarr)
            r=heapq.heappop(self.symbarr)
            #construct a new symbol with frequency = to the summation of the two symbols
            #value is 'a' dummy valuue just to know that it is a constructed symbol
            node=symbol.Symbol('a',l.frequency+r.frequency,l.probability+r.probability)
            #keep the two symbols in the left and the right of the new node
            node.left=l 
            node.right=r
            #pudh the new node
            heapq.heappush(self.symbarr,node)
        printCodes(self.map,self.symbarr[0],"")
        
        
    def PrintCodeTable(self,codeTable):
        print('huffman printCodeTables')
        with open (codeTable,'w') as wf:
            for ( key, value ) in self.map.items():
                wf.write( str(key)) #shofy hna hy7sl moshkela wla eh 
                wf.write(' ')
                wf.write(value)
                wf.write('\n')
            
                
                
    def EncodeMessage(self,message,encodedMessage):
        print('huffman encodemessage')
        with open (encodedMessage,'w') as wf:
            for i in message:
                wf.write(self.map[i])
            
    
            
                