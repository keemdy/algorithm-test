import sys
from itertools import combinations
from collections import Counter
input = sys.stdin.readline

n = int(input())
array = Counter(map(int, input().split()))
# array = list(map(int, input().split()))

count = 0

for i, j, k in combinations(array, 3):
    if j*2 == k + i:
        count += 1
print(count)
