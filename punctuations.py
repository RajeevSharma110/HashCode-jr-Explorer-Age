# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:16:05 2021

@author: naman
"""

test_str = "HELLO, welcome to : hashcode ! (a LEJHRO initative) ;"
 

print("The original string is : " + test_str)
 
#punctuations
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
# Removing punctuations in string
# Using loop + punctuation string
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, "")
 
# printing result
print("The string after punctuation filter : " + test_str)