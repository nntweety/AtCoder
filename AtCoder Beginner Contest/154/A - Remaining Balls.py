S, T = map(str, input().split())
S_num, T_num = map(int, input().split())
U = input()

if U == S:
  S_num -= 1
else:
  T_num -= 1

print(str(S_num) + " " + str(T_num))