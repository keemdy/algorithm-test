from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 최소 기울이기 몇 번
n, m = map(int, input().split())
board = []

for i in range(n):
    temp = input().rstrip()
    for j in range(len(temp)):
        if temp[j] == 'B':
            br, bc = i, j
        elif temp[j] == 'R':
            rr, rc = i, j
    board.append(temp)

visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque([(rr, rc, br, bc, 1)])

visited[rr][rc][br][bc] = True

def move(r, c, dr, dc):
    cnt = 0
    while board[r + dr][c + dc] != '#' and board[r][c] != 'O':
        r, c = r + dr, c + dc
        cnt += 1
    return r, c, cnt

def bfs():
    while q:
        rr, rc, br, bc, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            next_rr, next_rc, cnt_r = move(rr, rc, dr[i], dc[i])
            next_br, next_bc, cnt_b = move(br, bc, dr[i], dc[i])
            if board[next_br][next_bc] == 'O':
                continue
            if board[next_rr][next_rc] == 'O':
                return depth
            if next_rr == next_br and next_rc == next_bc:
                if cnt_r > cnt_b:
                    next_rr -= dr[i]
                    next_rc -= dc[i]
                else:
                    next_br -= dr[i]
                    next_bc -= dc[i]
            if not visited[next_rr][next_rc][next_br][next_bc]:
                visited[next_rr][next_rc][next_br][next_bc] = True
                q.append((next_rr, next_rc, next_br, next_bc, depth + 1))
    return -1
            
print(bfs())

