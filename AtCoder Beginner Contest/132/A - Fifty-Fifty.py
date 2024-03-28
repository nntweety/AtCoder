S = input()

def check(i):
    return i == 4

def checkHalf(str):
  flg = True

  if not check(len(str)):
    flg = False
    return flg

  firstStr = S[0]
  secondStr = ''
  strNum = 0

  for i in range(len(str)):
    if str[i] == firstStr:
      strNum += 1
    if S[i] != firstStr and not secondStr:
        secondStr = S[i]
    if secondStr != '':
      if S[i] != firstStr and S[i] != secondStr:
        flg = False
        return flg

  if(strNum != (len(S) / 2)):
    flg = False

  return flg

if checkHalf(S):
  print('Yes')
else:
  print('No')