import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0]*(n + 1) for _ in range(n + 1)]

# apple
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 1

l = int(input())

snakes = []
# 시간, 방향
for _ in range(l):
    t, d = input().split()
    snakes.append((int(t), d))

# 동 남 서 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def roate90(i, d):
    # 시계
    if d == 'D':
        i += 1
        if i == 4:
            i = 0
    # 반시계
    else:
        i -= 1
        if i == -1:
            i = 3
    return i

r, c = 1, 1
i = 0
idx = 0
time = 0
# 꼬리 위치
tail = [(r, c)]
while True:
    t = snakes[idx][0]
    if t == time and idx != len(snakes):
        i = roate90(i, snakes[idx][1])
        idx += 1
        if idx == len(snakes):
            idx -= 1
    nr, nc = r + dr[i], c + dc[i]
    # 벽 만나면 끝
    if not 0 < nr <= n or not 0 < nc <= n or board[nr][nc] == 2:
        time += 1
        break
    # 사과
    if board[nr][nc] == 1:
        board[nr][nc] = 0
        # 몸
        board[nr][nc] = 2
        tail.append((nr, nc))
        time += 1
        r, c = nr, nc
        continue
    # 사과 없는 ...!
    if board[nr][nc] == 0:
        tr, tc = tail.pop(0)
        board[tr][tc] = 0
        tail.append((nr, nc))
        board[nr][nc] = 2
        time += 1
        r, c = nr, nc
        continue


print(time)