# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:11:41 2018
@author: hagar
"""

import huffman
import symbol 

class Encoder: 
    def __init__(self,inputfile): #constructor in python
    #self must be passed to any method in the class
        self.inputFile=inputfile
        print('Encoder constructor')
        self.message=self.ReadFile()
        #create new huffman object !
        self.huffman=huffman.Huffman()
        #get unique vlaues in the message and put them in a list
        self.values=list(set(self.message))#list of unique bytes
        self.symbols=[]# list of symbols objects  # {} for dict (map) and [] for list (array)
        self.GenerateSymbols()
        
        
        
    def ReadFile(self):# don't forget self to be passed to any method in the class !! please XD
        #read file as binary file (in the form of bytes)
        print('Encoder readfile')
        with open (self.inputFile,'rb') as rf:
            fcontents= rf.read(3)
            fcontents=rf.read()
            #print(fcontents)
            return bytearray(fcontents) 
    
    def GenerateSymbols(self):
        print('Encoder generate symbols')
        i=0
        while i<len(self.values):
            #make new symbol object and pass the value,frequency and Probability to it
            self.symbols.append(symbol.Symbol(self.values[i],self.message.count(self.values[i]),self.message.count(self.values[i])/len(self.message)))
            i=i+1
            
    def Encode(self,codeTable,encodedMessage):
        print('Encoder Encode')
        #construct huffman tree
        self.huffman.HuffmanCodes(self.symbols)
        
        #print codetable into the file
        self.huffman.PrintCodeTable(codeTable)
        
        #print encoded message into the file
        self.huffman.EncodeMessage(self.message,encodedMessage)
        
        
        

#r=Encoder('Dataset_1.tsv')
#print(len(r.message))
#print(len(r.values))
#print(r.symbols[5])

#arr=b"abc"
#for value in arr:
#    print(value)
#print(arr)

#print(bytearray(arr))
#print(bin(r.message[0]))
#print(hex(r.message[0]))
#print(r.message[0])