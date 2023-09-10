N = int(input())
# 이진 탐색은 오름차순이 보장되어야 함
arr = sorted(list(map(int, input().split())))
M = int(input())
arr2 = list(map(int, input().split()))


def binary_search(target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        # 중점을 지정해서 찾아준다
        mid = (start + end) // 2
        # 원하는 값을 찾은 경우
        # print(start, mid, end)
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            # 중점이 찾으려는 값보다 크다면
            # -> 그 전까지 찾음
            end = mid - 1
        else:
            # 중점이 찾으려는 값보다 작다면
            # -> 그 뒤부터 찾음
            start = mid + 1
    return 0


for v in arr2:
    print(binary_search(v))
