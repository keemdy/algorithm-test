import sys
import heapq
input = sys.stdin.readline

n = int(input())
board = [[0]*n for _ in range(n)]
favor = dict()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check():
    total = 0
    for r in range(n):
        for c in range(n):
            if not board[r][c]:
                continue
            cnt = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if not 0 <= nr < n or not 0 <= nc < n:
                    continue
                if board[nr][nc] in favor[board[r][c]]:
                    cnt += 1
                    # print(cnt)
            if cnt == 1:
                total += 1
            elif cnt == 2:
                total += 10
            elif cnt == 3:
                total += 100
            elif cnt == 4:
                total += 1000
    return total

def seat(idx):
    q = []
    for r in range(n):
        for c in range(n):
            if board[r][c]:
                continue
            like_cnt, empty_cnt = 0, 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if not 0 <= nr < n or not 0 <= nc < n:
                    continue
                if board[nr][nc] in favor[idx]:
                    like_cnt += 1
                if not board[nr][nc]:
                    empty_cnt += 1
            heapq.heappush(q, (-like_cnt, -empty_cnt, r, c))
    like, empty, r, c = heapq.heappop(q)
    board[r][c] = idx


for i in range(n**2):
    temp = list(map(int, input().split()))
    favor[temp[0]] = set(temp[1:])

# 주변 탐색 후 차례대로 앉히기
for idx in favor.keys():
    seat(idx)

# 만족도
print(check())