import math
age, price = map(int, input().split())
free = 0
if age <= 5:
  print(free)
elif 6 <= age <= 12:
  print(math.floor(price / 2))
else:
  print(price)