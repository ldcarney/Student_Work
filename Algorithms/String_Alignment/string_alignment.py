#Liam Carney
#Algorithms
import numpy as np

"""
Recall that the string alignment problem takes as input two strings x and
y, composed of symbols xi, yj in sigma, for a fixed symbol set sigma, and returns a minimal-cost
set of edit operations for transforming the string x into string y.
"""

#Developing a cost Matrix, Optimal sequence of edit Operations, and Plagiarism Detector of two text files of song lyrics.

def alignStrings(x, y, cInsert, cDelete, cSub):
	
	#append '_' to both strings to form an optimal Cost Matrix
	x = '_' + x
	y = '_' + y

	#creates empty table for nx rows and ny collumns
	S = [[0 for j in range(len(y))] for i in range(len(x))]

	#sets all values in first row to column# * cost of operation
	for i in range(len(x)):
		S[i][0] = i * cInsert
	#sets all values in first column to row# * cost of operation
	for i in range(len(y)):
		S[0][i] = i *cInsert


	for i in range(1, len(x)):
		for j in range(1, len(y)):

			#no operation
			if x[i] == y[j]:
				S[i][j] = S[i-1][j-1]
				

			#subproblems
			else:
				delete = S[i-1][j] + cDelete
				insert = S[i][j-1] + cInsert
				sub = S[i-1][j-1] + cSub
				S[i][j] = min(sub, delete, insert)

	return S

				

def extractAlignment(S, x, y, cInsert, cDelete, cSub):

	nx = len(x)
	ny = len(y)
	arr = []

	#iterates unitl array reaches final row or collumn 
	while nx != 0 and ny != 0:


		#subproblems: determines which edit operation is found 
		if S[nx][ny] == S[nx][ny-1] + cInsert:
			arr.append('Insert')
			ny -= 1

		elif S[nx][ny] == S[nx-1][ny] + cDelete:
			arr.append('Delete')
			nx -= 1

			
		elif S[nx][ny] == S[nx-1][ny-1]:
			arr.append('No op')
			nx -= 1
			ny -= 1	
			

		elif S[nx][ny] == S[nx-1][ny-1] + cSub:
			arr.append('Sub')
			nx -= 1
			ny -= 1

	#in case row finishes before column or vice versa
	if nx == 0:
		for i in range(ny):
			arr.append('Insert')

	if ny == 0:
		for j in range(nx):
			arr.append('Delete')
		
	
	return list(reversed(arr))



def commonSubstrings(x, L, a):

	substring = []
	temp = []

	i = 0

	#Creates string of contnous 'no op' edit operations
	for op in a:
		if op == 'No op':
			#temporarily holds 'no op' element in array until array length is >= L
			temp.append(x[i])
			i += 1
			
		#transfers temp to substring if >= L
		elif op == 'Sub':
			i += 1
			if len(temp) > L:
				substring.append(temp)
			temp = []

		#transfers temp to substring if >= L
		elif op == 'Delete':
			i += 1
			if len(temp) > L:
				substring.append(temp)
			temp = []

		#transfers temp to substring if >= L
		elif op == 'Insert':
			if len(temp) > L:
				substring.append(temp)
			temp = []

	#in case temp >= L after while loop exits
	if len(temp) >= L:
		substring.append(temp)

	return substring 



#Problem A test Case
x = 'EXPONENTIAL'
y = 'POLYNOMIAL'
insertCost = 2
deleteCost = 1
subCost = 2

print("A. Cost Matrix of", x, "and", y, ":")
S = alignStrings(x, y, insertCost, deleteCost, subCost)
for i in range(len(x)):
	row = []
	for j in range(len(y)):
		row.append(S[i][j])
	print(row)

arr = (extractAlignment(S, x, y, insertCost, deleteCost, subCost))

print("\n A. Optimal Sequence of Edit Operations for", x, "and", y, ":\n", arr)
#print(commonSubstrings(x, 3, arr))


#Problem C
def plagDetect(song1, song2, cInsert, cDelete, cSub):

	with open(song1, 'r') as s1:
		x = s1.read().replace('\n', '')

	with open(song2, 'r') as s2:
		y = s2.read().replace('\n', '')

	S = alignStrings(x, y, cInsert, cDelete, cSub)
	arr = extractAlignment(S, x, y, cInsert, cDelete, cSub)
	substring = commonSubstrings(x, 10, arr)

	for i in substring:
		sub = ""
		for j in i:
			sub += j
		print(" ", len(i), " ", sub, "\n")
	


song1 = "Song1_Folsom_Prison.txt"
song2 = "Song2_Crescent_City_Blues.txt"

c_insert = 1
c_delete = 1
c_sub = 1

print("\n C. Plagiarism Detector:")

plagDetect(song1, song2, c_insert, c_delete, c_sub)










