def factorial(k):
    if k == 0:
        return 1
    return k*factorial(k-1)
n = int(input('Enter n:'))
m = int(input('Enter m:'))

while ((n>0) and (m>=0)):

    def Combi(n,m):
        if m == 0:
            return 1
        if n == m:
            return 1
        else:
            return Combi(n-1,m) + Combi(n-1,m-1)



    def Combif(n,m):
        a = factorial(n)/(factorial(m)*factorial(n-m))
        return a

    print("Combif(%d, %d) = %d" %(n,m, Combif(n,m)))
    print("Combi(%d, %d) = %d" %(n, m, Combi(n,m)))

    n = int(input('Enter n:'))
    m = int(input('Enter m:'))

