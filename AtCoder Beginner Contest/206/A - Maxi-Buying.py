import math;
N = int(input())
price = math.floor(N * 1.08)
standard = 206

if price > standard:
  print(':(')
elif price == standard:
  print('so-so')
else:
  print('Yay!')