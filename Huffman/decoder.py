# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:12 2018

@author: hagar
"""

#import os
#import bitarray

class Decoder:
    def __init__(self,codeTable,encodedFile,decodedFile):
        self.codeTable=codeTable
        self.encodedFile=encodedFile
        self.decodedFile=decodedFile
        self.map={} #interpretted not compiled take care
        self.ReadCodeTable()
        self.stream=self.ReadFile()
#        self.Message=bytearray()
        self.Message=[]
        self.DecodeHuffman()
        self.FinalMessage=bytearray()
        self.DecodeUTF8()
            
    def ReadCodeTable(self):
        s=""
        with open (self.codeTable,'r') as f:
            for line in f:
                s+=line
        r=s.split(' ')
        print(r)
        print (len(r))
        i=0;
        while i<(len(r)-1):
            self.map[r[i+1]]=r[i]
            i+=2
        print(len(self.map))
        
        n=list(self.map)
        print(n)
#        os.remove('codetables//c1.tsv')
            
        
                
    def ReadFile(self):
        print('Decoder ReadFile')
        #eof char is e so don't read after it is found
        with open (self.encodedFile,'rb') as rf:
#            trash= rf.read(3)
#            print(trash)
            arr= bytearray(rf.read())
            print(len(arr))
            i=0
            bits=""
            while i<len(arr):
#                print(arr[i])
                for j in range (0,8):
                    if ((arr[i] &0b10000000>>j)==0):
                        bits+="0"
                    else:
                        bits+="1"
                i+=1
                        
            print (len(bits))
            print(bits)
        return bits
    
    def DecodeHuffman(self):
        i=0
#        eof=True
        t=""
        while ((i<len(self.stream)) ):
            t+=self.stream[i]
            if (self.map.get(t))==None:
                i+=1
                continue
            else:
                if (self.map.get(t)=="101"):
                    break
                print(self.map.get(t))
                self.Message.append(int(self.map.get(t))) #message deh tb2a array 3adya wla byte array
                t=""
                i+=1
        print(self.Message)
        
    def DecodeUTF8(self):
        i=0
        while i<len(self.Message):
            pass
                
            
            
        
                
                
d=Decoder('codetables//codetable_t2.tsv','encoding//encoded_t2.tsv','decoding//DataSet_t2.tsv')

#my_var = d.map.get('101')
#print(my_var)
#t=int(my_var)
#i=int(my_var,10).to_bytes(1,byteorder='big')
#print(i)
#print(type(i))
#x=bytearray()
#x.append(t)
#print(x)




#print(chr(i))
#h=hex(i)
#print(h)
#print(type(h))


#empty_bytes = bytes(4)
#print(type(empty_bytes))
#print(empty_bytes)

#print(bytes(my_var))

