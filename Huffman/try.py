## -*- coding: utf-8 -*-
#"""
#Created on Fri Apr 27 19:12:12 2018
#
#@author: hagar
#"""
#
##import os
#import bitarray
#
#class Decoder:
#    def __init__(self,codeTable,encodedFile,decodedFile):
#        self.codeTable=codeTable
#        self.encodedFile=encodedFile
#        self.decodedFile=decodedFile
#        self.map={} #interpretted not compiled take care
#        self.ReadCodeTable()
#        
##        self.encodedMessage=
#        self.ReadFile()
#        
#        
#        
#    def ReadCodeTable(self):
#        s=""
#        with open (self.codeTable,'r') as f:
#            for line in f:
#                s+=line
#        r=s.split(' ')
##        print(r)
#        print (len(r))
#
#        i=0;
#        while i<(len(r)//2):
#            self.map[r[i+1]]=r[i]
#            i+=1
#        print(len(self.map))
#        n=list(self.map)
##        print(n)
#
##        os.remove('codetables//c1.tsv')
#            
#        
#                
#    def ReadFile(self):
#        #eof char is e so don't read after it is found
#        with open (self.encodedFile,'rb') as rf:
#            arr= bytearray(rf.read(3))
#            arr= bytearray(rf.read())
#            print(arr[1])
#            charr=chr(arr[1])
#            print(charr)
##            print (arr)
##            print(chr(str(arr[0])))
#            print (len(arr))
#            strarr=[]
#            
#            for i in arr:
#                strarr.append(str(i))
##            print(strarr)
#            
#            ba =bitarray.bitarray()
##            ba.frombytes(str(charr))
#            print(type(charr))
##            print(ba)
#            
##            bytestr =""
##            for i in arr:
##                bytestr+= str(i)
##            print(bytestr)
#            
##            x="".join(map(chr,arr))
##            print(x)
##            for i in x:
##                print(i)
##                
##            ba = bitarray.bitarray()
###byte_str='abc'
##            ba.frombytes(arr)
##            print(ba)
##            with open('dummy','w')as dummy:
##                dummy.write(bin(arr))
#
#            
#            
#            
#        
#                
#                
#d=Decoder('codetables//codetable_1.tsv','encoding//encoded_1.tsv','decoding//DataSet_1.tsv')
#
##d=Decoder('codetables//c1.tsv')
#
##binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
##text = binary_data.decode('utf-8')
##print(text)
#
##import bitarray
##ba = bitarray.bitarray()
##byte_str=bytes('1')
##ba.frombytes(byte_str)
##print(ba)
#
#
##bytes = ['112', '52', '52']
##i = []
##j=0
##while j<len(bytes):
##    
##    i.append(int (bytes[j]))
##    j+=1
##x="".join(map(chr, i))
##print(len(x))
##
##for k in x:
##    print(k)
#
#a = bitarray.bitarray()
#a.frombytes(b'a')
#print(a)
##bitarray('10000010')

#bytes = [112,52,52]
#s="".join(map(chr,bytes))
#print(s)

with open ('habl.tsv','w') as wf:
    #xef 239
    #xbb 187
    #xbf 191
    bytes = [239,187,191,112,52,52,216,167]
    bytes.append(112)
    s="".join(map(chr,bytes))
    print(s)    
    wf.write(s)


