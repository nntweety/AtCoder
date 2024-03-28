A,B= map(int, input().split())
max_value = max(A + B, A - B, A * B)
print(max_value)