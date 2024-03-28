import math
num, debris = map(int, input().split())

appleNum = (num * 3) + debris

print(math.floor(appleNum / 2))