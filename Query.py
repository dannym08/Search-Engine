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
    '''Processes queries on the index. '''
    def __init__(self):
        self.index = None
        self.json_data = get_url()
        
    def load_index(self, path = '/Users/Danny/Desktop/hw/cs121hw3/Index/', fileName = 'Index'):
        ''' '''
        with open(path+fileName, 'rb') as f:
            self.index = pickle.load(f)
       
    def get_query(self):
        ''' '''
        user_query = input("Please enter your query. Hit enter when finished: ")
        return user_query
    
    def tokenize_query(self, uQuery):
        tQuery = tokenize(uQuery)
        return tQuery
    
    def process_query(self, query):
        '''query is a list '''
        
        try:
            results = self.index[query[0]]
        except KeyError:
            pass
        
        #print(len(results))
        if len(query) == 1: return results
        results = sorted(results, key = lambda x : x[1])
        query = query[1:]

        for item in query: # deals with multi word queries
            intersect = list()
            i, j = 0, 0
            temp = None
            try:
                temp = sorted(self.index[item], key = lambda x : x[1])
                #print(len(temp))
                if temp != None:
                    while True:
                        try:
                            #print(results[i], temp[j])
                            index1, index2 = results[i][1], temp[j][1]
                            #print(index1, index2)
                        except IndexError: # One of them have finished
                            break
                        
                        if (index1 == index2):
                            intersect.append([results[i][0] + temp[j][0], index1]) # add both tf-idf's 
                            i+=1
                            j+=1
                        elif (index1 > index2):
                            j += 1
                        elif (index1 < index2):
                            i += 1
                        #print(intersect)
                        #input()
                    results = intersect
            except KeyError:
                print("Error, no query found, implement later.")
                
        return sorted(intersect, reverse = True) # TEST INTERSECT
            
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