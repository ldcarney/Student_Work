#Liam Carney
#Algorithms

import random
"""
Recursion algorithm to find Optimal value and Greedy value of card game where 
players choose value from right end or left end of array. Lowest value wins.
"""

#function to consider left side
def optLeft(A, p12, p, r, Final):

	#base case
	if r == p+1:
		#minimum of last two cards
		low = min(A[p], A[r])
		p12 += low
		r -= 1
		#if last card is reached, add to array of solutions
		Final.append(p12)


		return p12, p, r, Final


	#optimal chooses left side
	p12 += A[p]
	p += 1

	#greedy algorithm moves index
	if A[p] <= A[r]:
		p += 1

	else:
		r -= 1		

	return p12, p, r, Final

#function to consider right side
def optRight(A, p12, p, r, Final):
	
	#base case
	if r == p+1:
		#minimum of last two cards
		low = min(A[p], A[r])
		p12 += low
		r -= 1
		#if last card is reached, add to array of solutions
		Final.append(p12)
		return p12, p, r, Final
	
	#optimal chooses right side
	p12 += A[r]
	r -= 1

	#greedy algorithm moves index
	if A[p] <= A[r]:
		p += 1

	else:
		r -= 1

	return p12, p, r, Final
		
#Finds and stores most optimal sum for the current iteration in the recurrsion
def game(A, pCurrent, p, r, pTable, Final):
	pRight= 0
	pLeft = 0
	
	#while the the pointers are not at the same index
	if r > p:
	
		#Case for choosing right element
		pRight, f, l, Final = optRight(A, pCurrent, p, r, Final)
		#Case for choosing left element	
		pLeft, p, r, Final = optLeft(A, pCurrent, p, r, Final)


		#If a more optimal solution exists for a certain index, choose that one
		if pRight < pTable[f][l][0] or pTable[f][l][0] == -1:
			#sets current index to lower sum
			pTable[f][l][0] = pRight
			#recurrsion
			game(A, pRight, f, l, pTable, Final)

		if pLeft < pTable[p][r][0] or pTable[p][r][0] == -1:
			#sets current index to lower sum
			pTable[p][r][0] = pLeft
			#recurrsion
			game(A, pLeft, p, r, pTable, Final)

	

	return pTable, Final

	

def simulation():

	#creates array of random intigers
	A = []
	for i in range(100):
	  	A.append(random.randrange(0,100))

	#Array that will hold the values of all of the final Sums of each outcome
	Final = []
	#player one
	pOne = 0
	#first element
	p = 0
	#last element
	r = len(A)-1

	#creates table of len(A) x len(A) full of -1 to hold empty position
	pTable = [[[-1] for i in range(len(A))] for i in range(len(A))]

	#Starts the game
	pTable, Final = game(A, pOne, p, r, pTable, Final)
	
	#Optimum sum of cards for player one
	OptVal = min(Final)
	#Sum of cards for player two using the Greedy Algorithm
	GreedVal = sum(A) - OptVal

	#returns the Table, Optimum Value for player one, and value for greedy algorithm
	return pTable, OptVal, GreedVal


Table, OptVal, GreedVal = simulation()

print("The Optimal value is:", OptVal)
print("The Greedy Value is:", GreedVal)





