#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from nltk import RegexpTokenizer
"""
Helper functions
"""

def get_url():
    '''Parse json_data and return a dictonary'''
    file = '/Users/Danny/Desktop/hw/cs121hw3/WEBPAGES_RAW/bookkeeping.json'
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