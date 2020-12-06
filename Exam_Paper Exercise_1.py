# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:10:34 2020

@author: kitti
"""
class Snumpy():
#snp.ones(Int) : the ones function takes an int parameter and returns an array (list) of length
#int parameter and the array contains only ones
    def ones(self, num):
        array_of_ones = list([1] * num)
        return array_of_ones

#snp.zeros(Int): similar to the ones function, expect returns an array of zeros instead of ones

    def zeros(self, num):
        array_of_zeros = list([0] * num)
        return array_of_zeros
    
    
#snp.reshape(array, (row, column)) : takes an array and converts it into the dimensions specified
#by the tuple (row, column). Hence this function converts from a vector to a matrix
    
    def reshape(self, vector, rctuple):
        vector_size = len(vector)
        row = rctuple[0]
        column = rctuple[1]
        size_per_row = vector_size//row
        size_per_col = vector_size//column
        #check if the array size and the dimensions match
        if vector_size % row == 0 and vector_size % column == 0:
            for x in range(row): 
                if x == 0:              
                    first_row = list(vector[x:size_per_row])
                    matrix = list([first_row])
                else:
                    next_row = list(vector[x*size_per_row:(x+1)*size_per_row])
                    matrix.append(next_row)
            return matrix
        else:
            raise ValueError('The given dimensions do not match the array size!')
                
#snp.shape(array) : returns a tuple with the matrix/vector’s dimension e.g. (# rows, # columns)
    def shape(self, array):
              no_of_rows = len(array)
              
              if isinstance(array[0], list):   
                  no_of_cols = len(array[0])
                  result = (no_of_rows,no_of_cols)
                  #print('The input array is a matrix with these dimensions: \n {} rows, {} columns'.format(no_of_rows,no_of_cols))
                  return result
              else:
                  result = no_of_rows
                  #print('The input array is a vector with these dimensions: \n {} rows, 1 column'.format(no_of_rows))
                  return result
#snp.append(array1, array2) : returns a new vector/matrix that is the combination of the two
#input vectors/matrices. Note that you can’t append a vector to a matrix and vice versa and
#therefore use suitable exception handling and throw/return user friendly error messages
    def append(self, array1, array2):
        
        input1 = list(array1)
        input2 = list(array2)
        no_of_rows_1 = len(array1)
        no_of_rows_2 = len(array2)
        
        if isinstance(array1[0], list):
            no_of_cols_1 = len(input1[0])
            no_of_cols_2 = len(input2[0])
            
            #check if the two matrices have the same dimensions
            if no_of_rows_1 != no_of_rows_2 or no_of_cols_1 != no_of_cols_2:
                raise ValueError('The input matrices don\'t have the same number of dimensions.')
            else:
                #the result of appending the two matrices
                result = input1
                for row in input2:
                    result.append(row)
                return result
        else:
            #the result of appending vectors
            result = input1 + input2
            return result
        
#snp.get(array, (row, column)) : returns the value specified by the coordinate point (row, col-
#umn) of the array provided (can be vector or matrix).
    def get(self, array, rctuple):
        input_a = list(array)
        row_pos_user = rctuple[0]
        col_pos_user = rctuple[1]
        #check if the input for row dimension is interpretable in the context - not less than 0
        #or bigger than the length of the number of rows
        if row_pos_user > 0 and row_pos_user <= len(input_a):
            row_pos = rctuple[0]-1
            
            #check if array is two dimensional = a matrix
            if isinstance(input_a[0], list):
                #check if the input for column dimension is interpretable in context - not less
                # than 0 or bigger than the length of the number of columns
                if col_pos_user > 0 and col_pos_user <= len(input_a[0]):
                    col_pos = rctuple[1]-1
                    result = 'The matrix element of row {}, column {}: {}'.format(row_pos_user,col_pos_user,input_a[row_pos][col_pos])
                    return result
                else:
                    raise ValueError('The value given for the column dimension is invalid!')
            #returning value from a vector
            else:
                result = 'The vector element of row {}: {}'.format(row_pos_user,input_a[row_pos])
                return result
        else:
            raise ValueError('The value given for the row dimension is invalid!')
        
#snp.add(array1, array1) : addition on vectors/matrices        

    def add(self, array1, array2):
        input1 = list(array1)
        input2 = list(array2)
        shape_array1 = Snumpy.shape(self, input1)
        shape_array2 = Snumpy.shape(self, input2)
    
        if isinstance(array1[0], list) & isinstance(array2[0], list):
            #adding matrices
            #check if the input matrices have the same dimensions
            if shape_array1[0] != shape_array2[0] or shape_array1[1] != shape_array2[1]:
                raise ValueError('The input matrices don\'t have the same number of dimensions.')
            else:
                addition = []
                add_row = []
                zip_object = zip(input1, input2)
                for input1_i, input2_i in zip_object:
                    zip_object2 = zip(input1_i, input2_i)
                    for input1_j,input2_j in zip_object2:
                        
                        add_row.append(input1_j+input2_j)
                    addition.append(add_row)
                    add_row = []     
                return Snumpy.printMatrix(self, addition)
        else:
            #adding vectors
            #check if the input vectors have the same lenghts
            if shape_array1 != shape_array2:
                raise ValueError('The input arrays don\'t have the same dimensions.')
            result = np.array([sum(x) for x in zip(input1,input2)])     
            return result
        
#snp.subtract(array1, array1) : subtraction on vectors/matrices

    def subtract(self, array1, array2):
        shape_array1 = Snumpy.shape(self, array1)
        shape_array2 = Snumpy.shape(self, array2)
        input1 = list(array1)
        input2 = list(array2)
        if isinstance(input1[0], list) & isinstance(input2[0], list):
            #substracting matrices
            #check if the input matrices have the same dimensions
            if shape_array1[0] != shape_array2[0] or shape_array1[1] != shape_array2[1]:
                raise ValueError('The input matrices don\'t have the same number of dimensions.')
            else:
                difference = []
                diff_row = []
                zip_object = zip(input1, input2)
                for input1_i, input2_i in zip_object:
                    zip_object2 = zip(input1_i, input2_i)
                    for input1_j,input2_j in zip_object2:
                        diff_row.append(input1_j-input2_j)
                    difference.append(diff_row)
                    diff_row = []      
                return Snumpy.printMatrix(self, difference)
        else:
            #adding vectors
            #check if the input vectors have the same lenghts
            if shape_array1 != shape_array2:
                raise ValueError('The input arrays don\'t have the same dimensions.')
            difference = []
            zip_object = zip(input1, input2)
            for input1_i, input2_i in zip_object:
                    difference.append(input1_i-input2_i)
            result = difference        
            return result
        
#snp.dotproduct(array1, array1) : computes the dot product between two arrays (which could
# be vector or/and matrix) and returns an appropriate value. Use appropriate exception handling
# to output user-friendly error messages in case the dot product cannot be performed between
# the given arrays.
    def dotproduct(self, array1, array2):
        shape_array1 = Snumpy.shape(self, array1)
        shape_array2 = Snumpy.shape(self, array2)
        input1 = list(array1)
        input2 = list(array2)
        
        #matrices
        if isinstance(input1[0], list) & isinstance(input2[0], list):
            #matrices
            #check if the input matrices have the same dimensions
            if shape_array1[0] != shape_array2[0] or shape_array1[1] != shape_array2[1]:
                raise ValueError('The input matrices don\'t have the same number of dimensions.')
            else:
                length = shape_array1[0]*shape_array1[1]
                vector_of_zeroes = Snumpy.zeros(self, length)
                result_matrix = Snumpy.reshape(self, vector_of_zeroes, shape_array1)
                #iterate through rows of the first input
                for i in range(len(input1)):
                    # iterate through columns of the second input
                    for j in range(len(input2[0])):
                        # iterate through rows of the second input
                        for k in range(len(input2)):
                            result_matrix[i][j] += input1[i][k] * input2[k][j]
                return Snumpy.printMatrix(self, result_matrix)
        #vectors
        else:
            dot_product = 0
            for i in range(len(input1)):
                dot_product = dot_product + input1[i] * input2[i]
            return dot_product
            