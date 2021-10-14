# 순열
def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            # 다음 번에 추가시킬 원소값으로는 i번 째를 포함하지 않겠다.
            for next in permutations(array[:i] + array[i+1:], r-1):
                yield [array[i]] + next

for i in permutations([1, 2, 3, 4], 2):
    print(i, end=" ")