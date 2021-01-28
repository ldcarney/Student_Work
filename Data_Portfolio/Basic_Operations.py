#Liam Carney
#Data Cleaning and Simple Computations 


import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#%matplotlib inline
import statistics as stat

#A method to investigate the sensitivity of the sample mean and sample median 
#to extreme outliers and changes in the dataset is to replace one or more elements 
#in a given dataset by a number  𝑦 and investigate the effect when  𝑦 changes. 
#To illustrate this, consider the following dataset: [4.3, 5.2, 5.0, y, 3.8, 4.1, 5.5, 1.9]

#A.
#Finding mean for different subsitutes of y
y = 1.5
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
mean = stat.mean(sample)
median = stat.median(sample)
print("A.")
print("mean for y = 1.5:",mean,"\nmedian for y = 1.5:",median)

y = 6
sample2 = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
mean = stat.mean(sample2)
median = stat.median(sample2)
print("\nmean for y = 6:",mean,"\nmedian for y = 6",median)

#B.
#finding a value of y to get a desired mean of 6
y = 18.2
sample2 = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
mean = stat.mean(sample2)
#determining if we can maipulate mean to equal 6
median = stat.median(sample2)
print("\nB.")
print("There is a value of y to make the mean equal to 6:  y = ",y,"     mean =",mean)
print("\nThere is no value of y that would make the median equal to 6 because the middle number will remain between\n4.2 and 4.65.")

#C.
#computing sample variance and sample standard deviation for data set, y = 6.
print("\nC.")
y = 6
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
var = stat.variance(sample)
stdDev = stat.stdev(sample)
print("Sample Variance:",var,"\nStandard Deviation:",stdDev)


#D.
#Sample Median for values cases of y
print("\nD.")
y = 5
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
med = stat.median(sample)
print("median when y =5:",med)

y = 50
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
med = stat.median(sample)
print("median when y =50:",med)

y = 4.36
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
med = stat.median(sample)
print("median when y =4.36:",med)

y = float('inf')
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
med = stat.median(sample)
print("median when y = ∞:",med)

y = float('-inf')
sample = {4.3,5.2,5.0,y,3.8,4.1,5.5,1.9}
med = stat.median(sample)
print("median when y = -∞:",med)


#E
#Function for mean and variance
print("\nE.")
def my_sample_mean(array):
    sum1 = sum(array)
    mean = (sum1/len(array))
    return (mean)
def my_sample_var(array):
    x = my_sample_mean(array)
    newData = np.subtract(array, x)
    squared = np.power(newData, 2)
    addSquared = np.sum(squared)
    result = np.divide(addSquared, 11)
    return(result)


A = [98, 26, 83, 56, 60, 39, 81, 19, 72, 78, 94, 42]

mean = my_sample_mean(A)
var = my_sample_var(A)

print("Mean: ", mean)
print("Variance: ", var)



