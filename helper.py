#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from nltk import RegexpTokenizer
"""
Created on Mon Mar  4 18:10:50 2019

@author: Danny
"""

def get_url():
    '''Parse json_data and return a dictonary'''
    #file = '/Users/Danny/Desktop/cs121hw3/WEBPAGES_RAW/bookkeeping.json' #mac
    file =  r'C:\Users\Danny\Desktop\cs121hw3\WEBPAGES_RAW\bookkeeping.json'
    with open(file, 'r') as f:
        json_data = json.load(f)
    return json_data

def tokenize(text, docID = -1):
    '''Tokenize the text and return it.'''
    # Add stop words (look into just normal numbers)
    t = RegexpTokenizer("[\w']+")
    tokens = t.tokenize(text)

    if docID == -1 :
        tokens = [token.lower() for token in tokens]
    else: 
        tokens = [ [token.lower(), docID] for token in tokens if len(token) > 3]
        
    return tokens

def inverseDocID(docID):
    ''' '''
    file = docID % 500
    folder = docID // 500
    return str(folder), str(file)