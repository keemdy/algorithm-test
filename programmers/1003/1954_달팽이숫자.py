import sys
readline = sys.stdin.readline


n = int(input())

steps = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solution(n):
    i = 0
    r, c = 0, -1
    num = 0
    visited = [[0]*n for _ in range(n)]
    while num < n*n:
        d = steps[i]
        nr, nc = r + d[0], c + d[1]
        if not 0 <= nr < n or not 0 <= nc < n or visited[nr][nc]:
            i += 1
            if i > 3:
                i = 0
        else:
            num += 1
            r, c = nr, nc
            visited[r][c] = num
        answer = []
    return visited

for line in solution(n):
    print(line)
