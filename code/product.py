# 중복 순열

def product(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in product(array, r-1):
                yield [array[i]] + next

for i in product([1,2, 3, 4], 2):
    print(i, end=' ')