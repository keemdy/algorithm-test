import sys
from itertools import combinations
input = sys.stdin.readline

# 도시 크기, 폐업 치킨집 개수
n, m = map(int, input().split())
board = []
house = []
chicken = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            house.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))
    board.append(temp)

# 집 == 1, 치킨 == 2
# r, c = 1, 1
# 치킨 거리(가장 가까운 치킨집 사이의 거리)
# 도시의 치킨 거리 == 모든 집의 치킨 거리 합
def check_distance(cr1, cc1, cr2, cc2):
    return abs(cr1 - cr2) + abs(cc1 - cc2)

answer = 0
check = 0
sum_total = int(1e9)

for combi in list(combinations(chicken, m)):
    answer = 0
    for i in house:
        total = int(1e9)
        # answer = 0
        for c in combi:
            total = min(check_distance(i[0], i[1], c[0], c[1]), total)
        answer += total
    sum_total = min(answer, sum_total)
print(sum_total)
# 가장 작은 도시의 치킨 거리
