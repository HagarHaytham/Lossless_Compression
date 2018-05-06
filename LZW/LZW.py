# -*- coding: utf-8 -*-

class LZW:
    def __init__(self,inputfile): #constructor in python
        self.dictionary = []
        self.encoded_version = []
        self.formatefile(inputfile);
        self.encodedfile();
    
    def encodeLzw(self,input_string):
        print("algo")
        for char in input_string:
            if char in self.dictionary:  
                continue
            else:
                self.dictionary.append(char)
        self.dictionary.sort()
        #no_input = len(dictionary)
        next = ""
        
        #print(self.dictionary)
        for char in input_string:
            a = next + char
            if a in self.dictionary:
                 next = a
                 print("yaaaaaaaah")
            else:
                next = a[len(a)-1]
                dictionary_word = a[0:len(a)-1]
                print("a7eeh");
                self.dictionary.append(a)
                self.encoded_version.append(self.dictionary.index(dictionary_word))
        self.encoded_version.append(self.dictionary.index(next))
        #print(self.dictionary)
        
         
    
    def decodeLzw(self,encoded_version ):
        x = ""    
        for i in encoded_version:
            x = x + self.dictionary[i]
        return x
    
    def formatefile(self,file):
        #binary_data = bytes(file)  # ASCII values
        #temp = ""
        #i=0
       # while(i<len(file)):
         #   temp += str(file[i])
          #  i+=1
        #bytesenc = int(temp,2).to_bytes((len(temp)//8),byteorder='big')
        #text = binary_data.decode('utf-8')
       # bytes = [112, 89, 52]
        print(len(file))
        s="".join(map(chr, file))
        print("formatefile")
        self.encodeLzw(s)
    #==============================================================================
    #             i=0
    #             temp = ""
    #             while(i<len(arr)):
    #                  temp += str(arr[i] & 0b1)
    #                  for j in range (0,8): #check
    #                      if((arr[i] & 0b10000000>>j) == 0):
    #                          temp += "0"
    #                      else:
    #                          temp += "1"
    #                  i += 1
    #============================================================================
            
            
    def encodedfile(self):
        print("out file")
        with open ("output.tsv",'w') as wf:
            
            i=0;
            temp = ""
            while(i<len(self.encoded_version)):
                temp += str(self.encoded_version[i])
                temp += " "
                i += 1
            wf.write(temp)
            
            
        with open ("dictionary.tsv",'w') as wf:
            
            i=0;
            temp = ""
            while(i<len(self.dictionary)):
                temp += str(self.dictionary[i])
                temp += " "
                i += 1
            wf.write(temp)
         
            
           
           
                
    


