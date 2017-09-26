n = int(input("Enter n: "))
m = int(input("Enter m: "))

def factorial(n,m):
    if n<m:
        return 0
    else:
        return 1 if m == 0 else factorial(n-1,m)+factorial(n-1,m-1)

def fact2(n):
    if n == 0:
        return 1
    return n*factorial(n-1)



print(factorial(n,m))
print(fact2(n)/(fact2(n-m)*fact2(m)))