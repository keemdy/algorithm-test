n, m = map(int, input().split())
a, b, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
# 북 동 남 서 (시계방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
turn_time = 0
def direction():
    global d
    d -= 1
    if d == -1:
        d = 3
visited = [[False]*m for _ in range(n)]
answer = 1
r, c = a, b
visited[r][c] = True
while True:
    direction()
    # print(d)
    nr, nc = r + dr[d], c + dc[d]
    if not 0 <= nr < n or not 0 <= nc < n:
        continue
     # 가보지 않은
    if not board[nr][nc] and not visited[nr][nc]:
        r, c = nr, nc
        print(r, c)
        visited[r][c] = True
        turn_time = 0
        answer += 1
        continue
    # 방문했던 곳이거나 바다를 만나면
    else:
        turn_time += 1
    if turn_time == 4:
        nr, nc = r - dr[d], c - dr[d]
        if board[nr][nc] == 1:
            break
        turn_time = 0
        r, c = nr, nc

print(answer)