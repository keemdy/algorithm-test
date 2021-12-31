# 카운터 안 쓰면 시간초과남 ㅡㅡ
import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
array = Counter(map(int, input().split()))
# array = list(map(int, input().split()))
start = 1
end = max(array)
answer = 0

while start <= end:
    total = 0
    mid = (start + end)//2
    for val, freq in array.items():
        if val > mid:
            total += (val-mid)*freq
    # 미달, 왼쪽 탐색
    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)