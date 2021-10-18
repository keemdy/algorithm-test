import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = list(map(int, input().split()))

# 블루레이의 개수를 가급적 줄이려고 한다
# 녹화 가능한 길이를 최소로 하려고 한다.
# 단, M개의 블루레이는 모두 같은 크기이어야 한다.
start = max(board)
end = sum(board)
answer = []

while start <= end:
    total, cnt = 0, 1
    mid = (start + end)//2
    for x in board:
        if total + x > mid:
            cnt += 1
            total = 0
        # total + x가 기준(mid)보다 항상 작거나 같아야 함
        total += x
    # 미달
    if cnt <= m:
        end = mid - 1
    else:
        answer.append(mid)
        start = mid + 1

print(start)

