#Liam Carney
#Aglorithms
"""
Write a Python code for an algorithm, which takes as input a positive
integer n, randomly shuffles an array of size n with elements [1, ...., n] and
counts the total number of  counts the total number of flips in the shuffled array.
Also, run your code on a bunch of n values from [2, 2^2, 2^3, ... 2^20] and present your
result in a table with one column as the value of n and another as the number of
flips. Alternatively, you can present your table in form of a labeled plot with the
"""

import random
def shuffle(list):
    flips = 0
    random.shuffle(list)
    length=len(list)
    for i in range(0,length):
        for j in range(i,length):
            if list[i]>list[j]:
                flips= flips + 1
    return flips
#main method
print('Size','                Flips')
size = 2

while size <= 2**12:
    list=[i for i in range(1,size)]
    flips = shuffle(list)
    size*= 2
    print('%-20d %d' %(size,flips))

#problem 1c
"""
We say that A is sorted if A has no flips. Design a sorting algorithm
that, on each pass through A, examines each pair of consecutive elements. If a
consecutive pair forms a flip, the algorithm swaps the elements (to fix the out of
order pair). So, if your array A was [4,2,7,3,6,9,10], your first pass should swap
4 and 2, then compare (but not swap) 4 and 7, then swap 7 and 3, then swap 7
and 6, etc. Formulate pseudo-code for this algorithm, using nested for loops.
"""
def swap(list2):
    flips = 0
    temp = 0
    #random.shuffle(list)
    length=len(list2)
    for i in range(0,length):
        for j in range(i,length):
            if list2[i]>list2[j]:
                flips+=1
                temp = list2[i]
                list2[i] = list2[j]
                list2[j] = temp
                
    return flips

list2=[1,8,9,7,3,4,6,5,2,10]
print('\n'"Problem 1c")
print("Original Array: ", list2)
flips = swap(list2)
print("Sorted Array: ", list2)




