# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
#import huffman
import decoder

# from encoder import encoder as en
#import sys
#print (sys.path)

import os

inputFile='files//DataSet_20.tsv'
encodedMessage='encoding//encoded_20.tsv'
codeTable='codetables//codetable_20.tsv'
decodedMessage='decoding//DataSet_20.tsv'

encoder1=encoder.Encoder(inputFile)
encoder1.Encode(codeTable,encodedMessage)

#for knowing the size of a file
inf=os.stat(inputFile).st_size
print(inf)
ct=os.stat(codeTable).st_size
print(ct)
enf=os.stat(encodedMessage).st_size
print(enf)

compression_ratio=(inf/(ct+enf))
print (compression_ratio)

d=decoder.Decoder(codeTable,encodedMessage,decodedMessage)


#Huffman1.printCodeTable(codeTable)

#huffman1=encoder1.Encode(codeTable,encodedMessage)

#el decoder ya5od file el codetable w yconstuct huffman tree
#w ba3d keda y decode el file