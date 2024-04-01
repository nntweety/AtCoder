a = input()
s = input()
S = input()
T = input()
hitNum = 0
for i in range(0, len(S)):
  if S[i] == T[i]:
    hitNum += 1
print(hitNum)