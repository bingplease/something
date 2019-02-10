import sys
sys.setrecursionlimit(99999999)

def fibhelper(x, array):
  if x == 0:
    return 0
  elif x == 1:
    return 1
  elif array[x] != -1:
    return array[x]
  else:
    array[x] = fibhelper(x-1, array) + fibhelper(x-2, array)
    print(array[x])
    return array[x]
def betterfib(x):

  array = []
  
  for i in range(0, x+1):
    array.append(-1)
  return fibhelper(x, array)
  print(array)

a = int(input())
print(0)
print(1)
betterfib(a)