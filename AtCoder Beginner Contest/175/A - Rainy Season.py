S = input()
rainy = 'R'
if rainy + rainy + rainy in S:
  print(3)
elif rainy + rainy in S:
  print(2)
elif rainy in S:
  print(1)
else:
  print(0)

