import sys
from collections import deque
# import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, block_num):
    q = deque([(sr, sc)])
    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[sr, sc]], []
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not 0 <= nr < n or not 0 <= nc < n:
                continue
            if not visited[nr][nc] and board[nr][nc] == block_num:
                block_cnt += 1
                visited[nr][nc] = True
                q.append((nr, nc))
                blocks.append([nr, nc])
            if not visited[nr][nc] and board[nr][nc] == 0:
                block_cnt += 1
                rainbow_cnt += 1
                visited[nr][nc] = True
                q.append((nr, nc))
                rainbows.append([nr, nc])
    for r, c in rainbows:
        visited[r][c] = False
    # heapq.heappush(pq, (-block_cnt, -rainbow_cnt, -sr, -sc))
    return [block_cnt, rainbow_cnt, blocks+rainbows]

def rotateLeft90(board):
    r_board = [b[:] for b in board]
    for i in range(n):
        for j in range(n):
            r_board[n-j-1][i] = board[i][j]
    return r_board

def gravity(board):
    # 행 끝부터
    for i in range(n-2, -1, -1):
        # 열 첫번째 부터 돌기
        for j in range(n):
            # 내릴 수 있는 블록
            if board[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and board[r+1][j] == -2:
                        board[r+1][j] = board[r][j]
                        board[r][j] = -2
                        r += 1
                    else:
                        break

def removeBlocks(blocks):
    for r, c in blocks:
        board[r][c] = -2

score = 0
while True:
    visited = [[False]*n for _ in range(n)]
    blocks = [] # 가능한 블록 그룹

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                find_blocks = bfs(i, j, board[i][j])
                if find_blocks[0] >= 2:
                    blocks.append(find_blocks)
    blocks.sort(reverse=True)
    if not blocks:
        break
    removeBlocks(blocks[0][2])
    score += blocks[0][0]**2
    gravity(board)
    board = rotateLeft90(board)
    gravity(board)

print(score)

