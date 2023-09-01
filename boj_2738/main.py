N, M = map(int, input().split())
m = [[0] * M] * N
for i in range(1, N*2+1):
    tmp = list(map(int, input().split()))
    d = (i-1) % N
    m[d] = [m[d][j] + tmp[j] for j in range(M)]
for x in m:
    print(' '.join(list(map(str, x))))
