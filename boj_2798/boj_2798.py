from itertools import combinations

N, M = map(int, input().split())
# print('N:', N, 'M:', M)

cards = list(map(int, input().split()))
# print('cards', cards)

# cards는 정렬이 보장되어 있지 않음

s = [sum(c) for c in combinations(cards, 3) if sum(c) <= M]

# https://velog.io/@yeseolee/python%EC%9C%BC%EB%A1%9C-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EC%A7%81%EC%A0%91-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
# def comb(data, r):
#     for i in range(len(data)):
#         if r == 1:
#             yield [data[i]]
#         else:
#             for j in comb(data[i+1:], r-1):
#                 yield [data[i]] + j
# s = [sum(c) for c in comb(cards, 3) if sum(c) <= M]

print(max(s))
