n = int(input("Enter a number : "))

def fac(n):
    while n > -1:
        if n == 1:
            return 1
        elif n > 1:
            return n * fac(n-1)
print(n,"! = ",fac(n))

