N = input()
seven_flg = False
for i in range(len(N)):
  if N[i] == '7':
    seven_flg = True
    break;
if seven_flg:
  print('Yes')
else:
  print('No')