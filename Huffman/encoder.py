# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:11:41 2018

@author: hagar
"""

#print("mn kalb el encoder no7adskom")

import huffman
import symbol

class Encoder: 
    def __init__(self,inputfile):
        self.inputFile=inputfile
        self.message=self.ReadFile()
        #create new huffman object !
        self.huffman=huffman.Huffman()
        self.values=list(set(self.message))
        self.symbols={}
        i=0
        while i<len(self.values):
            self.symbols[i]=symbol.Symbol(self.values[i],self.message.count(self.values[i]),self.message.count(self.values[i])/len(self.message))
            i=i+1
        
    def ReadFile(self):
        with open (self.inputFile,'rb') as rf:
            fcontents= rf.read()
            return bytearray(fcontents)
        

r=Encoder('DataSet_1.tsv')
print(len(r.message))
print(len(r.values))
print(r.symbols[5].probability)
#print(bin(r.message[0]))
#print(hex(r.message[0]))
#print(r.message[0])