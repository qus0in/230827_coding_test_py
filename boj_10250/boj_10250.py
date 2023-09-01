T = int(input())
# print(T)
for _ in range(T):
    H, W, N = map(int, input().split())
    # print(H, W, N)  # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지
    # H를 먼저 쌓고, W를 다음에 이동시킨다
    # print("N % H", N % H)  # 층수
    X = str((N-1) // H + 1).zfill(2)
    Y = (N - 1) % H + 1
    print(Y, X, sep="")
