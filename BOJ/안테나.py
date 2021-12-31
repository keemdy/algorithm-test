import sys
input = sys.stdin.readline

# 안테나로부터 모든 집까지의 거리의 총 합이 최소
n = int(input())
board = list(map(int, input().split()))
board.sort()

print(board[n//2-1]) if n%2 == 0 else print(board[n//2])
