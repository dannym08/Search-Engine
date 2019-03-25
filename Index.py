from nltk import RegexpTokenizer
from bs4 import BeautifulSoup
from collections import defaultdict
from math import log
import os 
import pickle
#helper functions
from helper import get_url
from helper import tokenize
from helper import inverseDocID


"""
Created on Sat Mar  2 11:32:30 2019

@author: Danny
"""

class Index:
    ''' Creates the index.'''
    def __init__(self, path):
        self.path = path
        self.numOfPages = 0
        self.json_data = get_url()
        self.index = defaultdict(list)
        
    def tf_idf(self):
        ''' Computes inverse docutment frequency and multiplies it by the term frequency '''
        for key, values in self.index.items():
            numInDoc = len(values)
            idf = log(self.numOfPages/numInDoc)
            for i in range(numInDoc):
                self.index[key][i][0] = values[i][0] * idf # multiplies idf by tf and stores it
            
    def create_index(self):
        '''Loops through all Urls in all subdirectories and uses other functions
        to create the index'''
        ignore_list = {".DS_Store", "bookkeeping.json", "bookkeeping.tsv"}
        for root, dirs, files in os.walk(self.path, topdown=False):
           for name in files:
               if name not in ignore_list:
                   self.numOfPages += 1
                   self.open_file(os.path.join(root, name))
        self.tf_idf()
        self.sort_index()
    
    def open_file(self, path):
        '''Opens the file and passes it to the parser.'''
        try:
            print(path)
            p = path.split('/')
            folder, file = int(p[-2]), int(p[-1])
            docID = (500 * folder) + file #docID modulo 500 gets id num. integer division by 500 gets file
            with open(path, 'r') as file:
                self.htmlparser(file, docID)
        except FileNotFoundError:
            print("Path: " + path + " not found.")
        
    def htmlparser(self, file, docID):
        ''' '''
        try:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text() # gets all text on the webpage
            
            folder, file = inverseDocID(docID) ## Adds the title to the text ( weight it later )
            text = text + '\n' + self.json_data[folder+'/'+file] ## add url to the text
    
            token = tokenize(text, docID)
            freq_dict = self.add_frequency(token, docID) #gives that one pages index back
            for key, value in freq_dict.items(): # adds individual ones to the index
                self.index[key].append(value)
        except UnicodeDecodeError:
            self.numOfPages -= 1
        
    def add_frequency(self, tokens, doctID):
        ''' '''
        d = defaultdict(lambda : [0]) ##list with int 0
        numOfWords = len(tokens)
        for token, docID in tokens:
            d[token][0] += 1
            if len(d[token]) == 1: d[token].append(docID)
        for key, value in d.items(): ## Turns frequency in tf
            d[key][0] = d[key][0] / numOfWords
        return d
    
    def save_index(self, fileName = 'Index'):
        ''' '''
        path = '/Users/Danny/Desktop/cs121hw3/Index/'
        with open(path + fileName, 'wb') as f:
            pickle.dump(self.index, f, pickle.HIGHEST_PROTOCOL)    
        
    def sort_index(self):
        ''' '''
        for k,v in self.index.items():
            self.index[k] = sorted(v, reverse = True)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        