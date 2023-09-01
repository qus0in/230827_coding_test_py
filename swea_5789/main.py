T = int(input())
# print(T)  # 테스트 케이스 개수
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, Q = map(int, input().split())
    # print(N, Q)
    # 인덱스가 0부터 시작하므로 번호의 혼란을 막기 위해 N+1개 생성
    # arr = [0] * (N+1)
    arr = ["0"] * (N+1)
    for i in range(1, Q+1):
        # print(arr)
        L, R = map(int, input().split())
        # print(L, R)
        # arr[L:R+1] = [i for _ in arr[L:R]]
        arr[L:R+1] = [str(i) for _ in arr[L:R+1]]
    # print(arr)
    print(' '.join((arr[1:])))
