A,B,C = map(int, input().split())
last = C-(A-B)
if(last >= 0):
  print(last)
else:
  print(0)