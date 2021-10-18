import sys
input = sys.stdin.readline

# 최대
n, c = map(int, input().split())
# 좌표
board = [int(input()) for _ in range(n)]
board.sort()
start = 1
end = board[-1] - board[0]
answer = 0

while start <= end:
    cnt = 1
    mid = (start + end)//2
    val = board[0]
    for i in range(1, n):
        if board[i] - val >= mid:
            val = board[i]
            cnt += 1
    # 카운트 부족
    if cnt < c:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1


print(answer)