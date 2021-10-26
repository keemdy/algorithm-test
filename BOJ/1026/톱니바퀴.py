from collections import deque
# N 0 S 1

array = [deque(map(int, input())) for _ in range(4)]
k = int(input())

# 1 시계, -1 반시계
# 회전 톱니바퀴 번호, 방향
stages = []
for _ in range(k):
    num, direction = map(int, input().split())
    stages.append((num, direction))

# print(array)
idx = 0
while True:
    num, d = stages[idx]
    # 2번과 6번만 비교
    # print(idx, num, d)
    check_left = array[num-1][2]
    check_right = array[num-1][6]

    array[num-1].rotate(d)
    direction = d
    # 왼쪽
    # 가까운 애부터 먼 애까지
    d = direction
    for i in range(num-2, -1, -1):
        if array[i][2] != check_right:
            d *= -1
            check_right = array[i][6]
            array[i].rotate(d)
        else:
            break
    # 오른쪽
    d = direction
    for i in range(num, 4):
        if array[i][6] != check_left:
            d *= -1
            check_left = array[i][2]
            array[i].rotate(d)
        # 같으면 회전 안 해요
        else:
            break
    idx += 1
    if idx == k:
        break

answer = 0
for i in range(4):
    if array[i][0] == 1:
        answer += (2**i)
# print(array)
print(answer)
# 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
# 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
# 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
# 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
