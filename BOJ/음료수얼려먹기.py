import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def dfs(sr, sc):
    if not 0 <= sr < n or not 0 <= sc < m:
        return False
    if not board[sr][sc]:
        board[sr][sc] = 1
        dfs(sr - 1, sc)
        dfs(sr + 1, sc)
        dfs(sr, sc - 1)
        dfs(sr, sc + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
