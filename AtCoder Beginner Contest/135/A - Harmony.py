import math
A,B = map(int, input().split())

def getNum(a,b):
  k = (a + b) / 2
  if(abs(a - k) == abs(b - k) and (a + b) % 2 == 0):
    return math.floor(k)
  else:
    return 'IMPOSSIBLE'

print(getNum(A, B))