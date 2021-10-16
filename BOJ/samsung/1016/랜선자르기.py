import sys
import bisect
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

start = 1
end = max(line)
result = 0
# 최대 랜선 길이
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for x in line:
        cnt += x//mid
    # count 부족
    if cnt < n:
        end = mid - 1
    else:
        # 적어도 k개 이상
        result = mid
        start = mid + 1

print(result)
