import time
import random
numlist = []
i = 0

def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    if n <= 1:
        return n
    else:
        numlist.append(numlist[i-1] + numlist[i-2])
    if i == n:
        return numlist[-1]

while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

