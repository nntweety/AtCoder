weather = input()
pattern = ['Sunny', 'Cloudy', 'Rainy']
if weather == pattern[0]:
  print(pattern[1])
elif weather == pattern[1]:
  print(pattern[2])
elif weather == pattern[2]:
  print(pattern[0])