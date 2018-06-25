# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:51:04 2018

@author: Manoj.Prabhakar
"""

import numpy as np

# numpy is the basic block of python libraries and it is incredibly fast. It is for all algebraic functions

# Python list to an array

mylist = [1,2,3]

np.array(mylist)

# To create matrices

myarr = [[1,2,3],[4,5,6],[7,8,9]]

np.array(myarr)

# Range function in numpy

np.arange(0,10)

np.arange(0,11,2)

np.zeros(3)

np.zeros((4,4))

np.ones((2,2))

np.linspace(0,5,10) # Evenly spaced points between starting value and ending value

# TO create an Identity Matrix

np.eye(4)

# To generate random samples of a uniform distribution

np.random.rand(5) 

# To get an array of two dimensional array of uniform distribution

np.random.rand(5,5)

# To get it from Normal distribution

np.random.randn(2)
    
np.random.randn(3,3)

# To get random integers from low number to high number (lowest is included and highest is excluded, last digit provides how many numbers we need)

np.random.randint(1,100)

np.random.randint(1,100,5)

arra = np.arange(0,16,1)

arra

# To reshape an array

arr=arra.reshape(4,4)

arr.shape

# Numpy array indexing

arra = np.arange(0,11)

arra[1]

arra[0:3]

arr[:5]

arra[5:]

arra[0:4]=100

arra

arra=np.arange(0,11)

slic_arra = arra[0:5]

slic_arra[:] = 99

slic_arra

arra

arra_copy = arra.copy()

arra

arra_copy

arra_copy[:] = 9

arra

arra_copy

arra_2d = np.array([[5,10,15],[20,25,30],[30,35,40]])

arra_2d

# To get individual value in an array

arra_2d[2][2]

# To get the entire row

arra_2d[1]

# Conditional Selection

arra = np.arange(1,11)

bool_arra = arra > 4

bool_arra

arra[bool_arra] # Conditionally select those values for which the condition is true

arra[arra>4]

# numpy operations

arra = np.arange(0,11)

arra+arra

arra - arra

arra * arra

arra + 100 

arra * 100

arra/arra # Only runtime warning and no error on executing the code

1/ arra

arra ** 2

# Universal aarray functions

np.sqrt(arra)

np.exp(arra)

np.max(arra)

np.sin(arra)

np.cos(arra)

np.log(arra)

#https://docs.scipy.org/doc/numpy-1.14.0/reference/ufuncs.html - To get all functions in numpy

# Questions

1. Create an array of 100 zeroes

2. Create an array of 10 Tens 

3. Create an identity matrix of 5*5

4. Create an array of integers between 10, 100

5. Create an 10* 10 matrix of 0 to 99

6. Random number from uniform distribution  

7. Random Number from Normal distribution

8. Guess the output

    np.arange(1,101,1).reshape(10,10)/100

9. Create 30 Linearly spaced points

10. Standard deviation of matrix
    




















