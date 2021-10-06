def solution(n):
    num = 0
    d = 0
    r, c = -1, 0
    steps = [(1, 0), (0, 1), (-1, -1)]
    visited = [[0]*n for _ in range(n)]
    
    while num < n*(n+1)//2:
        dir = steps[d]
        nr, nc = r + dir[0], c + dir[1]
        if not 0 <= nr < n or not 0 <= nc < n or visited[nr][nc]:
            d += 1
            if d > 2:
                d = 0
        else:
            num += 1
            r, c = nr, nc
            visited[r][c] = num
            
    return [c for r in visited for c in r if c != 0]