# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:07:31 2020

@author: kitti
"""

#Exercise 2 - Hamming Code

import numpy as np

#Part1
#Write a simple Hamming encoder program in Python, which when given a 4-bit binary value,
# returns the resulting 7-bit binary vector codeword. Also implement the 
# parity check functionality to see if there are any errors, that is to check
#  whether H ∗ codeword = −→ 0 holds, where −→ 0 is zero vector.


#put the parity check function into the encoder
def encoder(input_vector):
    G = np.array([[1,1,0,1],
                [1,0,1,1],
                [1,0,0,0],
                [0,1,1,1],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1]])
    codeword = G.dot(input_vector) % 2
    return codeword

def parity_check(codeword):
    H = np.array([[1,0,1,0,1,0,1],
                  [0,1,1,0,0,1,1],
                  [0,0,0,1,1,1,1]]) 
    zero = H.dot(codeword) % 2
    return zero

#Part2
# Create a decoder program in Python, which when given a 7-bit vector codeword, returns the
# original 4-bit vector word. That is, if we are given a 4-bit word (w), and we apply our
#  encoder to return a codeword (codeword = G ∗ word), 
# and then we apply the decoder matrix (R) (fig. 3) to codeword, 
# then it should return the original word, such that R * codeword = word
#@ is matrix multiplication
def decoder(codeword):
    R = np.array([[0,0,1,0,0,0,0],
                  [0,0,0,0,1,0,0],
                  [0,0,0,0,0,1,0],
                  [0,0,0,0,0,0,1]])
    #@ is matrix multiplication
    word = R@codeword
    return word

Vec = np.array([1,0,1,1])

