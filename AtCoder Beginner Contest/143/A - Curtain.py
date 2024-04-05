L, size = map(int, input().split())
rest = L - size * 2
if rest > 0:
  print(rest)
else:
  print(0)