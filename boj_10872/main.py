N = int(input())
# print(N)
dp = list(range(0, N+1))
dp[0] = 1
for n in range(2, N+1):
    dp[n] = dp[n-1] * dp[n]
print(dp[N])
