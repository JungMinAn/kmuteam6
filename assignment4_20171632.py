def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

n = int(input('Enter n:'))
m = int(input('Enter m:'))

Cf = factorial(n)/(factorial(m)*factorial(n-m))
print(Cf)

def Rfactorial(n,m):
    if n == 0:
        return 0
    else:
        return factorial(n-1)/(factorial(m)*factorial(n-m-1)) + factorial(n-1)/(factorial(m-1)*factorial(n-m))

print(Rfactorial(n,m))
