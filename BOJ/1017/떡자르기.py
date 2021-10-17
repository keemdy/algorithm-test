n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
answer = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    for x in array:
        if x > mid:
            total += x - mid
    # 길이 부족
    if total < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)