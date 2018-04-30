# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:11:41 2018

@author: hagar
"""

#print("mn kalb el encoder no7adskom")

import bitarray

import huffman
import symbol

class Encoder: 
    def __init__(self,inputfile): #constructor in python
    #self must be passed to any method in the class
        self.inputFile=inputfile
        self.message=self.ReadFile()
        #create new huffman object !
        self.huffman=huffman.Huffman()
        #get unique vlaues in the message and put them in a list
        self.values=list(set(self.message))#list of unique bytes
        self.symbols={}# list of symmbols objects
        self.GenerateSymbols()
       
        
    def ReadFile(self):# don't forget self to be passed to any method in the class !! please XD
        #read file as binary file (in the form of bytes)
        with open (self.inputFile,'rb') as rf:
            arr = bytearray(rf.read()) 
            print("old " + str(arr))
            
            #convert letter into one byte
            i=3
            while(i<len(arr)):
                 if(arr[i] & 0b10000000 == 0b0):
                     i += 1
                     continue
                 
                 temp = "1"
                 temp += str(arr[i] & 0b1)
                 for j in range (0,6): #check
                     if((arr[i+1] & 0b100000>>j) == 0):
                         temp += "0"
                     else:
                         temp += "1"
                         
                 arr[i] = int(temp,2) #convert into binary
                 del arr[i+1]
                 i += 1     
                 
            print("new " + str(arr))
            return arr
    
    def GenerateSymbols(self):
        i=0
        while i<len(self.values):
            #make new symbol object and pass the value,frequency and Probability to it
            self.symbols[i]=symbol.Symbol(self.values[i],self.message.count(self.values[i]),self.message.count(self.values[i])/len(self.message))
            i=i+1
        

r=Encoder('t1.tsv')
#print(len(r.message))
#print(len(r.values))
#print(r.symbols[5].probability)


#print(bin(r.message[0]))
#print(hex(r.message[0]))
#print(r.message[0])