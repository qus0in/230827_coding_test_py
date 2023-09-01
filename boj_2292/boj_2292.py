# 6, 12, 18, 24, 30, ...
N = int(input()) - 1
w = 1
while N > 0:
    N = N - (w * 6)
    # print(N)
    w += 1
print(w)
