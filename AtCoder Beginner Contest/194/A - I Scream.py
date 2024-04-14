A, B = map(int, input().split())
milk_solid = A + B
if milk_solid >= 15 and B >=8:
  print(1)
elif milk_solid >= 10 and B >= 3:
  print(2)
elif milk_solid >= 3:
  print(3)
else:
  print(4)