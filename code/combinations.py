# 조합
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r - 1):
                yield [array[i]] + next

for i in combinations([1, 2, 3, 4], 2):
    print(i, end=' ')