def fac(n,m):
    if (n==m):
        return result + 1
    elif (m==0):
        return result + 1


    else:
        return fac(n-1,m) + fac(n-1,m-1)
    print(fac(n,m))




def solution(n, m):
    up = 1;
    down1 = 1;
    down2 = 1;
    for i in range(1, n+1):
        up = up * i


    for i in range(1, m+1):
        down1 = down1 * i
        for i2 in range(1,n-m+1):
            down2 = down2 * i2


    answer = up/(down2*down1)
    return answer

n=int(input("n"))
m=int(input("m"))
a = solution(n,m)
print(a)