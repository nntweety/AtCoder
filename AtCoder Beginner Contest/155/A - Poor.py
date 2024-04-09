A, B, C = map(int, input().split())
equal_num = 0
if A == B:
  equal_num += 1
if A == C:
  equal_num += 1
if B == C:
  equal_num += 1
if equal_num == 1:
  print('Yes')
else:
  print('No')