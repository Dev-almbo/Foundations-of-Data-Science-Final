#!/usr/bin/env python3
# -*- coding: utf-8 -*-


## Hamming code by Allie 

import numpy as np 
import random 


# create message, with rows being the length of the vector to code
# we are re-creating the (7,4) - Problem, therefore rows must be 4
# the message is a 4-bit vector, that is a vector with 4 rows. 

#this  function creates a random message 

def message(rows):
    
    #input: rows represents the length of the message to be encoded
    # a list of randomly chosen 0s and 1s is converted into a numpy array 
    vector = np.array([random.choice([0,1]) for i in range(rows)])
    return vector
        
##1 Encoding 

def encoding(message):
        # input: vector that contains the message that is to be encoded
        # G is a 7x4 matrix because of the (7,4)-problem
        G = np.array([[1,1,0,1], 
                     [1,0,1,1], 
                     [1,0,0,0], 
                     [0,1,1,1], 
                     [0,1,0,0], 
                     [0,0,1,0], 
                     [0,0,0,1]])
    
        # calculate the dotproduct of the encoding matrix and the 4-bit vector
        # to get the vector with the encoded message
        c_message = np.dot(G, message)%2
        return c_message
   
##2 Parity check 

def parity_check(c_message):
    
        #input: vector that contains the encoded message
        # run a partiy_check to ascertain whether there is an error in the transmission
        # H is the 3 x 7 parity check matrix
        H = np.array([[1,0,1,0,1,0,1], 
                     [0,1,1,0,0,1,1], 
                     [0,0,0,1,1,1,1]])
    
        # the dot product of H and the encoded message must be zero
        # if there are no errrors in the encoded message 
        nullvector = np.dot(H, c_message)%2
        
        
        # notify the user if there is an error, and return the nullvector that is 
        # equivalent to the position of the bit that was false
        # there is an error when at least one element in the nullvector is non-zero
        if np.any(nullvector): 
            print('The encoded messages contains errors, the transmission has gone wrong.') 
        return nullvector
            
##3 Decoding      
    
def decoding(c_message): 
    
    # input: vector that contains the encoded message
    # R is the 4x7 decoder matrix because of the (7,4)-problem. 
    R = np.array([[0,0,1,0,0,0,0], 
                 [0,0,0,0,1,0,0], 
                 [0,0,0,0,0,1,0], 
                 [0,0,0,0,0,0,1]])
    
    # calculate the dotproduct of the decoding matrix and the vector 
    # with the encoded message to get the original message 
    message = np.dot(R,c_message)%2
    return message


# Example 1 - coded message correct

# create message 
mes_1 = message(4)

# encode message
c_mes1 = encoding(mes_1)

# run parity check 

parity_check(c_mes1)

# decode message

d_mes1 = decoding(c_mes1)


# Example 2 - coded message not correct
mes_2 = message(4)
c_mes2 = encoding(mes_2)
c_mes2 = np.array([1, 0, 1, 1, 1, 1, 0])  #encoding(message(4)) represents an error term
parity_check(c_mes2)