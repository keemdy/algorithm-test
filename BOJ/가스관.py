import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = []

# 일곱가지 블록
# +는 특별한 블록 (수평, 수직)
# 해커가 지운 블록 하나의 행과 열, 어떤 블록이었는지 구하기

# | - + 1 2 3 4

visited = [[False]*n for _ in range(m)]
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def direction(s):
    if s == '|':
        return [1, 3]
    elif s == '-':
        return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z':
        return [0, 1, 2, 3]
    elif s == '1':
        return [0, 1]
    elif s == '2':
        return [0, 3]
    elif s == '3':
        return [2, 3]
    elif s == '4':
        return [1, 2]

def bfs(r, c, dir):
    global final_r, final_c
    q = deque([(r, c, dir)])
    visited[r][c] = True

    while q:
        r, c, dir = q.popleft()
        for i in dir:
            nr, nc = r + dr[i], c + dc[i]
            if not 0 <= nr < m or not 0 <= nc < n or visited[nr][nc]:
                continue
            if board[nr][nc] != '.':
                visited[nr][nc] = True
                ndir = direction(board[nr][nc])
                q.append((nr, nc, ndir))
            # 가스관이 없다면 ?
            else:
                if board[r][c] == 'M' or board[r][c] == 'Z':
                    continue
                if final_r == 0 and final_c == 0:
                    final_r, final_c = nr + 1, nc + 1
                nd = (i+2)%4
                if nd not in candidates:
                    candidates.append(nd)

# 모스크바 -> 자그레브
mr, mc = 0, 0
zr, zc = 0, 0
candidates, final_r, final_c = [], 0, 0

for i in range(m):
    temp = input().strip()
    for j in range(len(temp)):
        if temp[j] == 'M':
            mr, mc = i, j
        elif temp[j] == 'Z':
            zr, zc = i, j
    board.append(temp)

bfs(mr, mc, [0, 1, 2, 3])
bfs(zr, zc, [0, 1, 2, 3])

for i in range(m):
    for j in range(n):
        if board[i][j] != '.' and not visited[i][j]:
            bfs(i, j, direction(board[i][j]))
candidates.sort()

pipe = ['|', '-', '1', '2', '3', '4']
if len(candidates) == 4:
    print(final_r, final_c, '+')
else:
    for p in pipe:
        if candidates == direction(p):
            print(final_r, final_c, p)