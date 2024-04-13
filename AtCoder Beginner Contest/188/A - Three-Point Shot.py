x, y = map(int, input().split())
loser = min(x, y)
winner = max(x, y)
if loser + 3 > winner:
  print('Yes')
else:
  print('No')