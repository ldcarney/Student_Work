#Liam Carney
#h-index


def index(A):
	n = len(A)-1
	if 0 < n:
		m = len(A)//2
		L = A[:m]
		R = A[m:]
		index(L)
		index(R)

		i, h = 0, 0
		for i in range(n):

			if A[i] >= i+1:
				h = i+1 

		return h

A = [12,4,3,0]

print("The Mad Scientists h-index is", index(A))
print("There are",index(A), "Papers, with at least", index(A), "citations.")

