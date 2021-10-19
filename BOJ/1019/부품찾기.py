import sys
input = sys.stdin.readline

n = int(input())
board_n = list(map(int, input().split()))
board_n.sort()
m = int(input())
board_m = list(map(int, input().split()))
board_m.sort()

def binary_search(target):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end)//2
        if board_n[mid] == target:
            print("yes")
            return
        if board_n[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print("no")

for b in board_m:
    binary_search(b)

