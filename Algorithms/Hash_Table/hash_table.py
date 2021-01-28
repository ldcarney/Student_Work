#Liam Carney
#Algorithms

import random
import matplotlib.pyplot as plt

#Hash Tables


def Hash(data, arrNameTemp, h1Temp, h2Temp, l):

	sum1 = 0
	sum2 = 0
	k = 0
	rand = []

	#creates a set of random values to use in Hash 2
	for i in range(l):
		rand.append(random.randrange(0, l-1))



	#reads each line in txt file and seprates the last name
	for line in data:
		info = line.split("\t")

		lastName = info[0]

		


		#calculates the index value (1-26) of each charcter of the current last name and sums them together
		for i in range(len(lastName)):

			#incriments through the list of random numbers
			k = k+1

			#compares current character of last name to each value on the alphabet until index value is found
			for j in range(len(Alph)):
				if Alph[j] == lastName[i]:
					
					#hash 1
					sum1 = sum1 + j
					#hash 2
					sum2 = sum2 + j*random.choice(rand)

		#finds the hash 1 value of each last name
		hashFunc1 = sum1 % l
		#finds the hash 2 value of each last name
		hashFunc2 = sum2 % l

		#assigns each hash 1 value to a list
		h1Temp.append(hashFunc1)

		#assigns each hash 2 value to a list
		h2Temp.append(hashFunc2)

		#assigns each name to a list
		arrNameTemp.append(lastName)

		#resets sum to 0 for next iteration 
		sum1 = 0
		sum2 = 0

	return plotHashOne(h1Temp, arrNameTemp), plotHashTwo(h2Temp, arrNameTemp)



def plotHashOne(h1Temp, arrNameTemp):

	#creates empty hash table
	hashTable = [[]for i in range(l)]
	hist = {}
	n = len(arrNameTemp)

	#randomly chooses a 50% of last names from .txt
	for i in range(int(n/2)):


		x = random.randrange(0, n)	

		#fills hash table with random last names
		hashTable[h1Temp[x]].append(arrNameTemp[x])

		#creates python dictionary of frequency of last names assigned to each hash value for histogram
		hist[h1Temp[x]] = hist.get(h1Temp[x], 0)+1
 	
 	#plots histogram with frequency of hashed last names
	plt.bar(hist.keys(), hist.values())
	plt.title('Hash One: Last Names')
	plt.xlabel('Bucket')
	plt.ylabel('Frequency')
	plt.show()

	return hashTable

def plotHashTwo(h2Temp, arrNameTemp):

	#creates empty hash table
	hashTable = [[]for i in range(l)]
	hist = {}
	n = len(arrNameTemp)

	#randomly chooses a last name within the txt file
	for i in range(int(n/2)):


		x = random.randrange(0, n)	

		#fills hash table with random last names
		hashTable[h2Temp[x]].append(arrNameTemp[x])

		#creates python dictionary of frequency of last names assigned to each hash value for histogram
		hist[h2Temp[x]] = hist.get(h2Temp[x], 0)+1
 	
 	#plots histogram with frequency of hashed last names
	plt.bar(hist.keys(), hist.values())
	plt.title('Hash Two: Last Names')
	plt.xlabel('Bucket')
	plt.ylabel('Frequency')
	plt.show()

	return hashTable


data = open("dist.all.last.txt")
arrNameTemp = []

h1Temp = []
h2Temp = []
l = 5987


Alph = ['/','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']	


HT1, HT2 = Hash(data, arrNameTemp, h1Temp, h2Temp, l)

#print Hash Table for Hash 1 (uses chaining)
print("Hash Table for Hash One:\n", HT1, '\n\n')
#print Hash Table for Hash 2
print("----------------------------------------------------------------------------------------------\n\n")
print("Hash Table for Hash Two:\n", HT2)






	



