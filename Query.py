#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
from helper import tokenize
from helper import get_url
from helper import inverseDocID
"""
Created on Mon Mar  4 22:25:04 2019

@author: Danny
"""

class Query:
 
    def __init__(self):
        self.index = None
        self.json_data = get_url()
        
    def load_index(self, path = '/Users/Danny/Desktop/cs121hw3/Index/', fileName = 'Index'):
        ''' '''
        with open(path+fileName, 'rb') as f:
            self.index = pickle.load(f)
            print(type(self.index))
       
    def get_query(self):
        ''' '''
        user_query = input("Please enter your query. Hit enter when finished: ")
        user_query = tokenize(user_query) 
        return user_query[0]
    
    def process_query(self, query):
        ''' '''
        try:
            return(self.index[query])
        except KeyError:
            print("Error, no query found, implement later.")
            
    def process_results(self, raw_results):
        ''' '''
        results = []
        for i in raw_results:
            folder, file = inverseDocID(i[1])
            url_index = folder + '/' + file
            url = self.json_data[url_index]
            results.append(url)
        return results

    def results_to_file(self, results, fileName =  "Results"):
        ''' '''
        path = '/Users/Danny/Desktop/cs121hw3/Results/'
        path += fileName
        with open(path, 'w') as f:
            for i in results:
                f.write(i + '\n')