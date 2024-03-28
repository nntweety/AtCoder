N,A,B = map(int, input().split())

def lower(n,a,b):
  trainPrice = n * a
  taxiPrice = b
  if(trainPrice > taxiPrice):
    return taxiPrice
  else:
    return trainPrice

print(lower(N,A,B))