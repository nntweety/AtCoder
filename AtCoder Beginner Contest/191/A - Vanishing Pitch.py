V, T, S, D = map(int, input().split())
distance = D / V
if distance < T or distance > S:
  print('Yes')
else:
  print('No')
