# 중복 조합

def combinations_with_replacement(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combinations_with_replacement(array[i:], r-1):
                yield [array[i]] + next


for i in combinations_with_replacement([1, 2, 3, 4], 2):
    print(i, end=" ")