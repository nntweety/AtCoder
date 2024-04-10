K = int(input())
A, B = map(int, input().split())
flg = False

if A % K == 0 or B % K == 0:
  flg = True

for i in range(A, B + 1):
  if i %  K == 0:
    flg = True
    break

if flg:
  print('OK')
else:
  print('NG')