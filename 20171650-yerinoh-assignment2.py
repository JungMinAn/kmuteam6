x = int(input("x를 입력하세요"))

def fac(x):
  if x>1:
    return (x*fac(x-1))
  else:
    return 1

print(fac(x))
