N, K = map(int, input().split())
S = input().strip()
print(S[:K - 1] + S[K - 1].lower() + S[K:])