def hand(a, b):
  if a == b:
    return a
  else:
    return 3 - a - b;

x, y = map(int, input().split())
print(hand(x, y));