#Liam Carney
#Algorithms

"""
Suppose we are given a set of non-negative distinct numbers S and a target t.
We want to find if there exists a subset of S that sums up to exactly t and the
cardinality of this subset is k.

Write a python program that takes an input array S, target t, and cardinality k, and
returns the subset with cardinality k that adds to t if it exists, and returns False
otherwise. Your algorithm needs to run in O(nt) time where t is the target and n is
the cardinality of S. In your code, provide a brief discussion of your runtime through
comments, referring to specific elements of your code.
"""

def subSum(S, t, k): 
    curr = False
    n = len(S)   
    #Creates a table of size n x t x k and initializes every position to False
    #O(n * t * k) time for the outer for loop runs n times, the immediate inner for loop runs t times and the inner most for loop runs k times
    Table=([[[False for i in range(k)] for j in range(t+1)]  for x in range(n+1)]) 
    
    
    #fills table for k = 1
    #Takes O(n * t) time
    for i in range(0, n):
        for j in range(0, t):
            
            #curr is set to true if S[x] equals current target
            if S[i] == j+1:
                curr = True
            else:
                curr = False

            if Table[i][j+1][0]:
                Table[i+1][j+1][0] = Table[i][j+1][0]
            else:
                Table[i+1][j+1][0] = curr   


    if k > 1:
        #fills table for k > 1
        #The nested for loops below run in O(n*t*k) this is the largest time consumer within the algorithm
        #and therefore sets the time complexity of the algorithm to O(n * t * k)
        for i in range(1, k):
            for x in range(0, n):
                for j in range(1, t + 1):
                    
                    #if current element in array is less than target
                    if S[x] < j:
                        #fill table with updated value of target, subtract one from cardinality
                        if Table[x][j - S[x]][i - 1]:
                            Table[x+1][j][i] = Table[x][j - S[x]][i - 1]
                        else:
                            Table[x+1][j][i] = Table[x][j][i]
                        
                    #if current element in array is less than target
                    else:
                        #set below table position to curr element
                        Table[x+1][j][i] =  Table[x][j][i]                
        
    
    #if subset exists
    if Table[n][t][k-1] == True:
        
        sub = []
        x = n - 1
        j = t
        i = k - 1
        #trace back until the subset is the size of the cardinality
        while(i >= 0):
                
                #checks if element in row is true, if so, move up a row.
            if Table[x][j][i] == True:
                x -= 1       

            else:
                sub.append(S[x])
                #subtracts element appended from target
                j = j - S[x]
                x -= 1
                i -= 1
                
        return sub

    else:
        return False
       
#Test Cases    
S = [2,1,5,7]
t = 4
k = 2
print("Input:", S, ", t =", t, ", k =", k, "\n Output:", subSum(S, t, k), '\n' )

S = [2,1,5,7]
t = 5
k = 1
print("Input:", S, ", t =", t, ", k =", k, "\n Output:", subSum(S, t, k), '\n' )

S =[2,1,5,7]
t = 6
k = 2
print("Input:", S, ", t =", t, ", k =", k, "\n Output:", subSum(S, t, k))







