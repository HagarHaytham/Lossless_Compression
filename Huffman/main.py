# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
#import huffman
#import decoder

# from encoder import encoder as en
#import sys
#print (sys.path)

import os


inputFile='files//DataSet_1.tsv'

inputFile1='files//t2.tsv'
encodedMessage='encoding//encoded_5.tsv'
encodedMessage1='encoding//encoded_t2.tsv'
codeTable='codetables//codetable_5.tsv'
codeTable1='codetables//codetable_t2.tsv'
decodedMessage='decoding//DataSet_4.tsv'

encoder1=encoder.Encoder(inputFile1)
encoder1.Encode(codeTable1,encodedMessage1)

#for knowing the size of a file
x=os.stat(inputFile).st_size
print(x)


#Huffman1.printCodeTable(codeTable)

#huffman1=encoder1.Encode(codeTable,encodedMessage)

#el decoder ya5od file el codetable w yconstuct huffman tree
#w ba3d keda y decode el file