# 테스트 케이스를 입력받는다
T = int(input())
# print('T', T)

# 테스트 케이스만큼 반복한다
for tc in range(1, T+1):
    # 테스트 케이스 순번을 표시한다
    # print('tc', tc)
    print(f'#{tc}', end=' ')
    # 메모리의 원래 값을 받는다
    memory = input()
    # print('memory', memory)
    # 수정한 횟수를 카운트할 변수를 준비한다 (count = 0)
    count = 0
    # print('count', count)
    # 직전 값과 일치하는지 비교할 이전 값 변수를 준비한다 (prev = 0)
    # prev = 0  # - 애초에 0이니까 0으로 준비한다 -> 에러난다!
    prev = '0'  # - 문자열로 준비했어야한다!
    # print('prev', prev)
    # 메모리의 원래 값을 순서대로 탐색한다
    for m in memory:
        # 현재 메모리값과 직전값을 비교한다
        if prev != m:  # 직전 값과 현재 메모리(비트) 값이 다른가?
            # 다르다면 count+=1 하고 prev를 해당 값으로 고쳐줌
            count += 1
            prev = m
            # print('*', end=' ')  # 메모리 체인지를 기록하여 시각화
        # print(m, end=' ')
    # print()
    # 수정한 횟수를 출력한다
    # print('after-count', count)
    print(count)
