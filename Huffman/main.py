# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:12:54 2018

@author: hagar
"""

import encoder
#import huffman
#import decoder2
import decoder

# from encoder import encoder as en
#import sys
#print (sys.path)

import os

inputFile='files//DataSet_20.tsv'
encodedMessage='encoding//encoded_20.tsv'
codeTable='codetables//codetable_20.tsv'
decodedMessage='decoding//DataSet_20.tsv'

#encodedMessage2='encoding2//encoded_1.tsv'
#codeTable2='codetables2//codetable_1.tsv'
#decodedMessage2='decoding2//DataSet_1.tsv'


encoder1=encoder.Encoder(inputFile)
encoder1.Encode(codeTable,encodedMessage)

#encoder2=encoder.Encoder(encodedMessage)
#encoder2.Encode(codeTable2,encodedMessage2)
#for knowing the size of a file
inf=os.stat(inputFile).st_size
print(inf)
ct=os.stat(codeTable).st_size
print(ct)

#ct2=os.stat(codeTable2).st_size
#print(ct2)
enf=os.stat(encodedMessage).st_size
print(enf)

compression_ratio=(inf/(ct+enf))
print ('compression ratio '+str(compression_ratio))

#d2=decoder2.Decoder2(codeTable2,encodedMessage2,decodedMessage2)
#d1=decoder.Decoder(codeTable,decodedMessage2,decodedMessage)

d1=decoder.Decoder(codeTable,encodedMessage,decodedMessage)


#Huffman1.printCodeTable(codeTable)

#huffman1=encoder1.Encode(codeTable,encodedMessage)

#el decoder ya5od file el codetable w yconstuct huffman tree
#w ba3d keda y decode el file