 

while 1<2: 
    fac =int(input("Enter a number: "))
    ans = 1
    if fac == -1:
        break
    else:
        for i in range(1,fac+1):
            ans *= i
        print(str(fac) + "! = " + str(ans))
