 -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:02:55 2018

@author: user
"""

# -*- coding: utf-8 -*-

class DecompressLZW:
    def __init__(self,encodedMessage,decodingMessage,dictionary1): #constructor in python
        self.dic = dictionary1
        self.decoded_version = []
        self.decodedfile = decodingMessage
        self.encodedfile = encodedMessage
        self.Readfile();
        self.outputfile();
    
    def Readfile(self,encodedfile):
         with open (encodedfile,'rb') as rf:
              arr = bytearray(rf.read())
         lzwdecode(arr)
              
    def outputfile(self,encodedfile):
         with open (encodedfile,'wb') as wf:
             
    
    def lzwdecode(self,indexarr):
        c = indexarr[0]
        w = self.dic[c]
        decoded_version.append(w)
        i = 1;
        while(i < len(indexarr)):
            c1 = indexarr[i]
            if c1 in self.dic: #index in dic ??!!
                w = self.dic[c1]
                self.dic.append(self.dic[c]+w[0])
            else:
                self.dic.append(self.dic[c]+w[0])
                w = self.dic[c1]
            decoded_version.append(w)
            c = c1
            i+=1