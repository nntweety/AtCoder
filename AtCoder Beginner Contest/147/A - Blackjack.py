A, B, C = map(int, input().split())
total = A + B + C
if total > 21:
  print('bust')
else:
  print('win')