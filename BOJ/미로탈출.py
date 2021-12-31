import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().rstrip())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 괴물 0, 없는 1
# 움직여야하는 최소 칸

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not 0 <= nr < n or not 0 <= nc < m or board[nr][nc] == 0:
                continue
            if board[nr][nc] == 1:
                q.append((nr, nc))
                board[nr][nc] += board[r][c]

bfs()
print(board[-1][-1])
