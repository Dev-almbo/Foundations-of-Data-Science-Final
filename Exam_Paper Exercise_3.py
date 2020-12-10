# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:12:26 2020

@author: kitti
"""

#Exercise 3

import numpy as np
import os

counterDict={}
separate_text_documents = {}
path = "Test_textfiles/"
all_files = os.listdir(path)
for file in all_files:
   # open the file and then call .read() to get the text
   text = []
   with open(os.path.join(path, file)) as f:
      for line in f:
   # removing their punctuation
        words = line.replace('.','').replace('\'','').replace(',','').lower().split()
        for word in words:
            text.append(word)
            if word not in counterDict:
                counterDict[word] = 1
            else:
                counterDict[word] = counterDict[word] + 1
   separate_text_documents[file] = text
   text = []


# creating a word vector for each document
def create_word_vectors(word_dict, documents):
    list_of_word_vectors = {}
    
    for file in documents:
        word_vector = []
        for key in word_dict:
            if key in documents[file]:
                word_vector.append(1)
            else:
                word_vector.append(0)
        list_of_word_vectors[file] = word_vector    
    return list_of_word_vectors

#provide a list of documents that are similar to the given search
# document, in descending order of their similarity with the search document

def examine_similarity(word_vectors,search_doc):
    #turn the search document into a word vector
    cleaned_search_doc = []
    words = search_doc.replace('.','').replace('\'','').replace(',','').lower().split()
    for word in words:
        cleaned_search_doc.append(word)
        
    search_doc_vector = []
    for key in counterDict:
        if key in cleaned_search_doc:
            search_doc_vector.append(1)
        else:
            search_doc_vector.append(0)
    
    #calculating the dot products between the search document and the list of documents
    results = {}
    for vector in word_vectors:
        dotproduct = np.dot(word_vectors[vector], search_doc_vector)
        results[vector] = dotproduct
    #order the list of documents into a descending order based on the dotproduct
    ordered_list = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
    return ordered_list.keys()