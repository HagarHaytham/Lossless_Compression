# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:12 2018

@author: hagar
"""

#import os
#import bitarray
import io

class Decoder2:
    def __init__(self,codeTable,encodedFile,decodedFile):
        self.codeTable=codeTable
        self.encodedFile=encodedFile
        self.decodedFile=decodedFile
        self.map={} #interpretted not compiled take care
        print('Decoder 2 Constructor')
        self.ReadCodeTable()
        self.stream=self.ReadFile()
#        self.Message=bytearray()
        self.Message=[]
        self.DecodeHuffman()
#        self.FinalMessage=bytearray()
        self.DecodeUTF8()
            
    def ReadCodeTable(self):
        s=""
        with open (self.codeTable,'r') as f:
            for line in f:
                s+=line
        r=s.split(' ')
#        print(r)
#        print (len(r))
        i=0;
        while i<(len(r)-1):
            self.map[r[i+1]]=r[i]
            i+=2
#        print(len(self.map))
        
        n=list(self.map)
#        print(n)
#        os.remove('codetables//c1.tsv')
            
        
                
    def ReadFile(self):
        print('Decoder 2 ReadFile')
        #eof char is e so don't read after it is found
        with open (self.encodedFile,'rb') as rf:
#            trash= rf.read(3)
#            print(trash)
            arr= bytearray(rf.read())
#            print(len(arr))
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
                        
#            print (len(bits))
#            print(bits)
        return bits
    
    def DecodeHuffman(self):
        print('Decode 2 Huffman')
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
                #print(self.map.get(t))
                self.Message.append(int(self.map.get(t))) #message deh tb2a array 3adya wla byte array
                t=""
                i+=1
        #print(self.Message)
        
#    def DecodeUTF8(self):
#        decint=[]
#        with io.open(self.decodedFile, 'w', encoding='utf-8') as fout:#, newline='\n'
#            i=0
#            while i<len(self.Message):
#                if (self.Message[i]& 0b10000000 == 0):#keda dah ascii
#                    decint.append(self.Message[i])
#                else:
#                    #print('No')
#                    temp="1101100"#d
#                    if (self.Message[i] & 0b01000000 ==0):
#                        temp+="0"
#                        #print('8')
#                    else:
#                        temp+="1"
#                        #print('9')
#                    k=int(temp,2) # convert it to int
#                    decint.append(k)
#                    temp="10"
#                    for j in range (0,6):
#                        if (self.Message[i] & 0b100000>>j)==0:
#                            temp+="0"
#                        else:
#                            temp+="1"
#                    k=int(temp,2)
#                    decint.append(k)
#            
#                i+=1
#            b=bytes(decint)
#            x=b.decode('utf-8')
#            fout.write(x)
#
#


#    def DecodeUTF8(self):
#        print('Decode 2 UTF8')
#        with open (self.decodedFile,'wb') as wf:
#            dec=""
#            for i in self.Message:
#                dec+=

    def DecodeUTF8(self):
#        decint=[]
        with io.open(self.decodedFile, 'w', newline='\n') as fout:
            b=bytes(self.Message)
            x=b.decode()
            fout.write(x)
                
                
#d=Decoder('codetables//codetable_1.tsv','encoding//encoded_1.tsv','decoding//DataSet_1.tsv')

