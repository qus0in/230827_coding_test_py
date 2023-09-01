def search(bd):
    n = len(bd)
    for r in range(n):  # 행방향 (세로)
        for c in range(n):  # 열방향 (가로)
            if bd[r][c] == '.':
                continue
            if c + 5 <= n:
                for b in board[r][c+1:c+5]:
                    if b == '.':
                        break
                else:
                    return True
            if r + 5 <= n:
                for b in [rl[c] for rl in board[r+1:r+5]]:
                    if b == '.':
                        break
                else:
                    return True
            if c + 5 <= n and r + 5 <= n:
                for i in range(1, 5):
                    b = board[r+i][c+i]
                    if b == '.':
                        break
                else:
                    return True
            if c - 5 <= n and r + 5 <= n:
                for i in range(1, 5):
                    b = board[r + i][c - i]
                    if b == '.':
                        break
                else:
                    return True
    return False


T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    N = int(input())
    board = []
    for _ in range(N):
        board.append(input().strip())
    print('YES' if search(board) else 'NO')