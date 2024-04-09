import math
N, M = map(int, input().split())
N_comb = math.comb(N, 2)
M_comb = math.comb(M, 2)
print(N_comb + M_comb)