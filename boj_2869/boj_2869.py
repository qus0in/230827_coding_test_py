A, B, V = map(int, input().split())
# print(A, B, V)

# A : 올라갈 수 있는 정도
# B : 얼마나 미끄러지는가
# V : 남은 높이

if A == V:
    print(1)
else:
    day = (V - B) // (A - B) + (1 if (V - B) % (A - B) else 0)
    print(day)
