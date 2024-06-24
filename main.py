#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 19:20:06 2024

@author: coco
"""
import math
import numpy

dataInput = input("Enter List of Data: ")
dataList = dataInput.split(",")
dataList = [int(digit) for digit in dataList]

print(dataList)

dataList.sort()

print(dataList)  # Output: [1, 2, 3, 4, 7]

minimum = min(dataList)
print("MINIMUM:", minimum)

if len(dataList) % 2 == 0:
    half = len(dataList)/2 # Focusing on the left half of the data array/list
    print("half even", half) #6.0 # Print how many elements we are focusing on (DEBUG)
    
    fourth = half/2 # 
    fourth = int(fourth) 
    
    print("fourth even",fourth)
    
    fourth -= 1 # indexes start from 0
    Q1 = dataList[fourth] #2
    print("FIRST QUARTILE (Q1):", Q1) #2
    
    # Calculate Q3
    Q3 = Q1 * 3
    print("THIRD QUARTILE (Q3):", Q3)
    
else:
    
    half = len(dataList)/2 # Focusing on the left half of the data array/list
    half -= .5 # Decimal is not extrenuous
    
    print("half odd", half) #6.0 # Print how many elements we are focusing on (DEBUG)
    
    fourth = half/2 #3.0 # Getting closer to Q1, the first quartile
    
    fourth = int(fourth) #3 # Indexes are integers
    
    print("int fourth", fourth) #3 # Print which element we are focusing on (DEBUG)
    #fourth -= 1 # indexes start from 0 # Now the index we are on is the 3rd
    num2 = dataList[fourth] #2 # Now the index we are on is the 4th in the list
    print("num2",num2) #2 
    
    fourth -= 1 #3?? # indexes start from 0 # Now the index we are on is the 3rd
    print("fourth-1", fourth) #3 # Print the 3rd index
    num1 = dataList[fourth] #3 
    print("num1" ,num1)#3
    Q1 = (num2 + num1)/2 #2.5
    
    print("FIRST QUARTILE (Q1):", Q1)#2.5
    
    print("fourth odd", fourth)
    
    # Calculate Q3
    Q3 = Q1 * 3
    print("THIRD QUARTILE (Q3):", Q3)
    

median = numpy.median(dataList)
print("MEDIAN:", median)  # Output: 3

maximum = max(dataList)
print("MAXIMUM:", maximum)

