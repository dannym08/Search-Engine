#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:34:59 2019

@author: Danny
"""
import tkinter as tk
from Query import Query
import webbrowser
from bs4 import BeautifulSoup

# load the query
Q = Query()
Q.load_index()
class SearchBar:
    
    def __init__(self):
        self.root = tk.Tk()
        #self.root.geometry("500x300")
        self.root.title("Danny's Search Engine")
        self.root.geometry(self.cetnerWindow()) 
        
        self.setup()
        self.root.mainloop()
        
    def setup(self):
        SearchLabel = tk.Label(self.root, text= "Welcome to Danny's Search Enginge").grid(row = 0, column = 0)
        self.searchBox = tk.Entry(self.root)
        self.searchBox.grid(row = 1, column = 0)
        self.searchB = tk.Button(self.root, text ="Search", command = self.searchButton)
        self.root.bind("<Return>", self.searchButton)
        self.searchB.grid(row = 2, column = 0)
        
        
    def searchButton(self, event = None):
        '''gets user query and creates results page '''
        user_query = self.get_query()
        if user_query != '':
            user_query = Q.tokenize_query(user_query)
            pQuery = Q.process_query(user_query)
            results = Q.process_results(pQuery)
            if len(results) == 0: #if no results
                root = tk.Tk()
                root.title("No Results Found.")
                l = tk.Label(root, text = "No Results were found.")
                l.pack()
            else: # If there are results
                rPage = ResultsPage(results, user_query)
        
    def get_query(self):
        return self.searchBox.get()
    
    def cetnerWindow(self, x = 0, y = 0):
        #screen_width = self.root.winfo_screenwidth()
        #screen_height = self.root.winfo_screenheight()
        #screen_resolution = str(screen_width)+'x'+str(screen_height)
        screen_resolution = "+" +str(x) + '+' + str(y)
        return screen_resolution
    

class ResultsPage:
    
    def __init__(self,results,  title = "Results"):
        self.index = 0
        self.maxIndex = len(results)
        self.title = title
        #self.root.geometry("300x200")
        self.results = results
        self.browser = webbrowser.get('safari')
        
        
        self.setup()
        self.root.mainloop()
        
    def nextButton(self, event= None):
        ''''''
        if (self.index >= self.maxIndex - 20):
            self.nextB.destroy()
        else:
            self.root.destroy()             
            self.index += 10
            self.setup()
        
    
    def lastButton(self, event = None):
        ''' '''
        if (self.index <= 9):
            self.lastB.destroy()
        else:
            self.root.destroy()
            self.index -= 10
            self.setup()
            
    def setup(self):
        ''' Use results to populate the page '''
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.geometry(self.cetnerWindow()) 
        self.nextB = tk.Button(self.root, text ="Next", command = self.nextButton, anchor = 'w')
        self.lastB = tk.Button(self.root, text = "Back", command = self.lastButton, anchor = 'e')
        
        curRow = 0
        for i in range(self.index, self.index + 10):
            link = tk.Label(self.root, text = self.results[i], fg="blue", cursor = "hand2")
            lb = tk.Label(self.root, text= str(i) + ") ")
            lb.grid(row = curRow, column = 0, padx = (10, 20))
            link.grid(row = curRow, column = 1, padx = (0, 10), pady= (10, 10))
            curRow += 1
            link.bind("<Button-1>", self.linkClick)
            
        self.lastB.grid(row = i+1, column = 0, sticky="E")
        self.root.bind("<BackSpace>",self.lastButton)
        self.nextB.grid(row = i+1, column = 1, sticky="E")
        self.root.bind("<Return>", self.nextButton)
        
    def linkClick(self, event):
        ''' '''
        url = event.widget.cget("text")
        self.browser.open(url, autoraise=True)
        
    def cetnerWindow(self, x = 0, y = 0):
        #screen_width = self.root.winfo_screenwidth()
        #screen_height = self.root.winfo_screenheight()
        #screen_resolution = str(screen_width)+'x'+str(screen_height)
        screen_resolution = "+" +str(x) + '+' + str(y)
        return screen_resolution