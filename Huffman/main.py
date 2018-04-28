# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
import huffman
import decoder
# from encoder import encoder as en
#import sys
#print (sys.path)



inputFile='DataSet_1.tsv'
encodedMessage='encoded.tsv'
codeTable='codetable.tsv'
decodedMessage='output.tsv'

with open (inputFile,'rb') as f:
    with open('test.tsv','wb')as wf:
        for line in f:
            wf.write(line)
#        size=10
#        fcontents=f.read()
#        #while len(fcontents)>0:
#        print(fcontents,end='')
#        #fcontents=f.read(size)