# 테스트 케이스를 입력받는다
T = int(input())

# 테스트 케이스만큼 반복한다
for tc in range(1, T + 1):
    print(f'#{tc}', end=' ')
    # 테스트케이스 별로 6장의 카드 순서 정보를 전달 받는다. (order)
    order = list(map(int, input().strip()))  # 순회를 돌 것이기 때문에 list 변환 필요
    # 플레이어가 가지고 있는 카드 번호별 수를 나타내는 리스트를 만든다. (hand)
    hand = [0] * 10  # 각각의 인덱스가 숫자에 대응한다 (0~9)

    # card를 임시변수로 하는 반복문으로 order를 탐색한다.
    for card in order:
        # card를 인덱스로 가지는 hand의 요소에 +1 해준다. (숫자를 카운트한다.)
        hand[card] += 1

    # hand를 체크하여 베이비 진인지 검사한다.
    # Triplet 카드들을 빼준다
    for i in range(len(hand)):
        while hand[i] >= 3:
            hand[i] -= 3
    # Run 카드들을 빼준다
    for i in range(len(hand) - 2):
        while hand[i] and hand[i+1] and hand[i+2]:
            hand[i] -= 1
            hand[i+1] -= 1
            hand[i+2] -= 1
    # 베이비 진이라면? -> 모두 제거되어서 총 합이 0일 것
    is_baby_gin = not sum(hand)
    print('true' if is_baby_gin else 'false')