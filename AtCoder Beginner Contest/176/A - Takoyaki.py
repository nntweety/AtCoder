import math
order_num, chunk, minute = map(int, input().split())
rotate = math.ceil(order_num / chunk)
print(rotate * minute)
