WEEK = ['SUN','MON','TUE','WED','THU','FRI','SAT']
TODAY = input()
TODAY_NUM = 0
for i in range(len(WEEK)):
  if WEEK[i] == TODAY:
    TODAY_NUM = i
print(len(WEEK) - TODAY_NUM)