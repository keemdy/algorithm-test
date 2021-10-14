import sys
input = sys.stdin.readline

# 블록 상하좌우 이동이 아니라 보드 90도 회전후 왼쪽으로 합침
# 최대 5번 이동, 얻을 수 있는 가장 큰 블록 출력
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def rotate(N, B):
    r_board = [b[:] for b in B]
    for i in range(N):
        for j in range(N):
            r_board[j][N-1-i] = board[i][j]
    return r_board

def convert(N, line):
    c_board = [i for i in line if i != 0]
    for i in range(1, len(c_board)):
        if c_board[i-1] == c_board[i]:
            c_board[i-1] *= 2
            c_board[i] = 0
    c_board = [i for i in c_board if i != 0]
    return c_board + [0]*(N-len(c_board))

def dfs(N, B, count):
    result = max([max(i) for i in B])
    if count == 0:
        return result
    for i in range(4):
        C = [convert(N, line) for line in B]
        result = max(result, dfs(N, C, count - 1))
        B = rotate(N, B)
    return result

print(dfs(n, board, 5))