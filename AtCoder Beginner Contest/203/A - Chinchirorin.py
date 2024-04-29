a, b, c = map(int, input().split())

if a == b:
  print(c)
  exit()
elif a == c:
  print(b)
  exit()
elif b == c:
  print(a)
  exit()
else:
  print(0)