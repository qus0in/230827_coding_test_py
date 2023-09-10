import sys

input = lambda: sys.stdin.readline().strip()

T = int(input())
# print(T)
data = [(i, input().split()) for i in range(T)]
# print(data)
print(*[' '.join(v[1]) for v
        in sorted(data,
        key=lambda x: (int(x[1][0]), x[0]))],
      sep='\n')
