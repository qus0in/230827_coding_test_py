T = int(input())  # 테스트 케이스 개수를 입력받음

# 각 테스트 케이스에 대한 반복문
for t in range(1, T+1):
    N = int(input())  # 노선의 개수를 입력받음
    # 노선 정보를 2차원 리스트로 입력받음
    # 각 노선의 시작과 끝을 나타내는 정류장 번호들이 2차원 리스트에 저장됨
    bn = [[int(ii) for ii in input().split()] for i in range(N)]

    P = int(input())  # 정류장의 개수를 입력받음

    bs = [0] * 5001  # 정류장을 나타내는 리스트를 생성하고 초기화
    for v in bn:
        # 노선의 시작부터 끝까지 해당하는 정류장을 1씩 증가시킴
        bs[v[0]:v[1]+1] = [el+1 for el in bs[v[0]:v[1]+1]]

    # 결과 출력
    # 출력 시 테스트 케이스 번호를 출력하고 공백을 붙임
    print(f"#{t}", end=' ')
    # 정류장 번호에 따른 결과를 리스트로 저장하여 출력
    result = [str(bs[int(input())]) for j in range(P)]
    # 결과 리스트를 문자열로 변환하여 출력하고 공백을 붙임
    print(' '.join(result), end=' \n')
