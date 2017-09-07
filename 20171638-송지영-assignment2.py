n=int(input("Enter a number: "))
factorial = 1
while n is not -1:
    for i in range(1, n+1):
        factorial = factorial*i
        if i == n:
            print(n,"! = ",factorial)
            n=int(input("Enter a number: "))
# kmuteam6
# kmuteam6
