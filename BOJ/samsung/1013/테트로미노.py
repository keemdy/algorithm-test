import sys
input = sys.stdin.readline

# 테트로미노 하나 적절히 놓기
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
# backtracking을 위해
max_num = max(map(max, board))
answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, idx, total):
    global answer
    if answer >= total + (3 - idx)*max_num:
        return
    if idx == 3:
        answer = max(total, answer)
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not 0 <= nr < n or not 0 <= nc < m or visited[nr][nc]:
            continue
        if idx == 1:
            visited[nr][nc] = True
            dfs(nr, nc, idx + 1, total + board[nr][nc])
            visited[nr][nc] = False
        visited[nr][nc] = True
        dfs(nr, nc, idx + 1, total + board[nr][nc])
        visited[nr][nc] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 0, board[i][j])
        visited[i][j] = False

print(answer)
