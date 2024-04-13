import math
distance, minute, speed = map(int, input().split())
if distance / speed <= minute:
  print('Yes')
else:
  print('No')
