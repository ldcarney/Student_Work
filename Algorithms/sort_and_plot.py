#Liam Carney
#Algorithms

import random
import matplotlib.pyplot as plt

#Sorting and Plotting Array


#sorting Algorithm for theta(n^2)
def flips(shuffledArr):
	#shuffledArr = generateNums()
	flips = 0
	length = len(shuffledArr)
	for i in range(0,length):
		j = i + 1
		for j in range(i,length):
			if shuffledArr[i]>shuffledArr[j]:
				#counts flips here
				flips= flips + 1
				#sorts array here
				shuffledArr[i], shuffledArr[j] = shuffledArr[j], shuffledArr[i]
	#returns the amount of flips
	return flips



#Sorting algorithm for theta(nlogn)
def mergeSort(A):
	count = 0
	flips = 0
	r = len(A)-1
	if 0 < r:
		#sets q to equal the middle of the array
		q = len(A)//2#int(r/2)
		#left side the of array
		B = A[:q]
		#right side of the array
		C = A[q:]
		#counts a flip for every time the array goes through a recursion 
		count += mergeSort(B)
		count += mergeSort(C)
		
		
		#merge(A,B,C)
		i, j, k = 0,0,0
		while i < len(B) and j < len(C):
			if B[i] <= C[j]:
				A[k] = B[i]
				i += 1
			else:
				A[k] = C[j]
				j += 1
				count += len(B) + j - k
			k += 1

		#checks for leftover flips to fix
		while i < len(B): 
			A[k] = B[i] 
			i+=1
			k+=1
		while j < len(C): 
			A[k] = C[j] 
			j+=1
			k+=1
	#returns the amount of flips
	return(count)

shuffledArr = []
shuffledArr2 = []
n2 = []
nlogn = []
#creates an array with lengths [2...2^12]
for i in range(1,12):
	n = 2**i
	for i in range(n):
		x = random.randint(1,20)
		shuffledArr.append(x)
		shuffledArr2.append(x)
	#adds the amount of flips to an array in order to insert in plot
	n2.append(flips(shuffledArr))
	nlogn.append(mergeSort(shuffledArr2))

#creates the plot comparing the num of flips for a Theta(n^2) algo and a Theta(nlogn) algo
my_bins = range(0, 1500, 150)
plt.hist(n2, bins=my_bins, edgecolor="white", facecolor = 'blue', alpha = .5, density = True)
plt.hist(nlogn,bins=my_bins, edgecolor="white", facecolor = 'red', alpha = .5, density = True)
plt.title("Theta(n^2) vs. Theta(nlogn): Number of flips ")
plt.xlabel('# of flips')
plt.ylabel('Frequency')
plt.legend(["Theta(n^2)", "Theta(nlogn)"])
plt.savefig('flips.png')
plt.show()
print(flips(shuffledArr))



	












