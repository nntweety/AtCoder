S = str(input())
digits = [int(digit) for digit in S]
flg = False
for i in range(1, len(digits)):
  if digits[i] == digits[i - 1]:
    flg = True
    break
if flg:
  print('Bad')
else:
  print('Good')