# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:02:55 2018

@author: user
"""

# -*- coding: utf-8 -*-

class CompressLZW:
    def __init__(self,inputfile,outputfile): #constructor in python
        self.dictionary = []
        #self.dictionary.append(0)
        self.n = ""
        self.out = outputfile
        self.encoded_version = []
        self.formatefile(inputfile);
        self.encodedfile();
        
    
    def encodeLzw(self,input_string):
        for char in input_string:
            if char in self.dictionary:  
                continue
            else:
                self.dictionary.append(char)
        self.dictionary.sort()
        self.n = ""
    
        for char in input_string:
            a = self.n + char
            if a in self.dictionary:
                 self.n = a
            else:
                self.n = a[len(a)-1] 
                dictionary_word = a[0:len(a)-1]
                self.dictionary.append(a)
                self.encoded_version.append(self.dictionary.index(dictionary_word))
        self.encoded_version.append(self.dictionary.index(self.n))
       
             
    def formatefile(self,file):
        print(len(file))
        s="".join(map(chr, file))
        print("formatefile")
        self.encodeLzw(s)
   
    def encodedfile(self):
        print("out file")
        with open (self.out,'wb') as wf:
            
            i=0;
            while(i<len(self.encoded_version)):
                y = self.encoded_version[i]*10
                z = y.to_bytes((y.bit_length() + 7) // 8, 'big')
                wf.write(z) 
                i += 1

         
            
           
           
                
    


