T = int(input())

for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, K = map(int, input().split())
    puzzle = []
    for n in range(N):
        puzzle.append(input().split())
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 행 방향
            if i - 1 < 0 or puzzle[i - 1][j] == '0':
                for r in range(i, i+K):
                    if r == N or puzzle[r][j] == '0':
                        break
                else:
                    if i+K == N or puzzle[i+K][j] == '0':
                        cnt += 1
            # 열 방향
            if j - 1 < 0 or puzzle[i][j-1] == '0':
                for c in range(j, j+K):
                    if c == N or puzzle[i][c] == '0':
                        break
                else:
                    if j+K == N or puzzle[i][j+K] == '0':
                        cnt += 1
    print(cnt)
