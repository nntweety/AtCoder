numlist = list(map(int, input().split()))
numlist.sort()
if numlist[1] * 2 == numlist[0] + numlist[2]:
  print('Yes')
else:
  print('No')