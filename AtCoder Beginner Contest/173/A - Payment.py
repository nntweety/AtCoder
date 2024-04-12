N = int(input())
surplus = N % 1000
if surplus == 0:
  print(0)
else:
  print(1000 - surplus)