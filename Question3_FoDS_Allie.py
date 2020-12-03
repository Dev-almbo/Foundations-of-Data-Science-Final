#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:46:18 2020

@author: allie
"""

import pandas as pd 
import numpy as np
import os 

# 1 function: read in files and compute dataframe with frequency 

def read_words(wrk_dir, filenames_list):
    os.chdir(wrk_dir) 
    
    # get words in each file in filenames_list
    overall_dict = {}
    for file in filenames_list:
        tmp_file = open(file, "r")
        tmp_words = tmp_file.read()
        temp_words = tmp_words.split()
        frequency = {}
        for item in temp_words:
            item = item.lower()
            for char in item:
                if char in ['.', ',','!','?', '(', ')','{','}','[',']', ';', '/']:
                    item = item.replace(char," ")
            # checking the element in dictionary
            if item in frequency.keys():
                # incrementing the count
                frequency[item] += 1
            else:
                # initializing the count
                frequency.update({item: 1})
        overall_dict.update({file: list(frequency.values())})
    
    return overall_dict

## 2 function calculate the distance 

def calculate_similarity(overall_dict_old, overall_dict_new):
    
    similarity_dict_dot = {}
    similarity_dict_euklid = {}
    for item in overall_dict_old.keys(): 
        # access vectors in ditionaries & make them numpy arrays
        vector_old = np.array(overall_dict_old[item])
        vector_new = np.array(overall_dict_new[list(overall_dict_new.keys())[0]])
        if len(vector_old) != len(vector_new): 
            print('The vectors do not have the same number of rows, a similarity cannot be computed.')
            return 
        # calculate similarity: dotproduct & euklid 
        result_dot = np.dot(vector_old, vector_new)
        result_euklid = np.linalg.norm(vector_old - vector_new)      
        
        # add each result to each specific dictionary 
        similarity_dict_dot.update({item: result_dot})
        similarity_dict_euklid.update({item: result_euklid})
    
    # make both dicts dataframes
        similarity_df_dot = pd.DataFrame(similarity_dict_dot)
        similarity_df_euklid = pd.DataFrame(similarity_dict_euklid)
    # join both dataframes together 
        similarity = zip(similarity_df_dot, similarity_df_euklid)
        return similarity 

### Testing Code
        
test_dir = "/Users/allie/Desktop/Universität/Master/Foundations of Data Science/Final/TestDir/" 
filenames_list = ['Testtext1.rtf', 'Testtext2.rtf']
test_old = read_words(test_dir, filenames_list)
new_file = ['Testtext3.rtf']
test_new = read_words(test_dir, new_file)

test_sim = calculate_similarity(test_old, test_new)

