import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
board = deque(list(map(int, input().split())))
visited = deque([False]*n)
# print(visited)
count = 1
while True:
    board.rotate(1)
    visited.rotate(1)
    visited[-1] = False
    for i in range(n-1, -1, -1):
        if not visited[i] and visited[i-1] and board[i] > 0:
            visited[i] = True
            visited[i-1] = False
            board[i] -= 1
    # print(board)
    visited[-1] = False

    if not visited[0] and board[0] > 0:
        board[0] -= 1
        visited[0] = True

    if board.count(0) >= k:
        break
    count += 1

print(count)