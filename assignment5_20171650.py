import time

def fibo(n) :
 if n == 1 or n == 2 :
     return 1
 return fibo(n - 1) + fibo(n - 2)

def iterfibo(n) :
     b = True
     f1 = 1
     f2 = 1

     while n > 2 :
         if b :
             f1 = f1 + f2
         else :
             f2 = f1 + f2

         b = not b
         n -= 1

     if b :
         return f2
     else :
         return f1

while True:
    nb = int(input("n: "))
    if nb == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nb)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nb, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nb)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nb, fibonumber, ts))