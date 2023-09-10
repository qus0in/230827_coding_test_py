M, N = map(int, input().split())
# print(M, N)
prime = [1] * (N+1)

# print(prime)
for i in range(2, N+1):
    if prime[i]:
        if i >= M:
            print(i)
        for j in range(i, N+1, i):
            # print(i, j)
            prime[j] = 0
# print(prime)

