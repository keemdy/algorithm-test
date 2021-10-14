import itertools

T = int(input())

def inspect(film, k):
    for L in film:
        layer = ''.join(L)
        if '1'*k not in layer and '0'*k not in layer:
            return False
    return True


def inject(film, d):
    for i in range(1, d+1):
        # 열 선택
        combi = itertools.combinations(tuple(range(d)), i)
        # A, B 선택
        pro = tuple(itertools.product(['0', '1'], repeat = i))

        for c in combi:
            film_copy = [layer[:] for layer in film]
            for p in pro:
                for idx, row in enumerate(c):
                    for m in range(w):
                        film_copy[m][row] = p[idx]
                    if inspect(film_copy, k):
                        return i
    return -1


for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    d, w, k = map(int, input().split())
    film = [[0]*d for _ in range(w)]
    # w x d
    for i in range(d):
        temp = input().split()
        for j in range(w):
            film[j][i] = temp[j]
    # print(d, w, k, film)
    # maxi = 0
    if k == 1 or inspect(film, k):
        # maxi = 0
        print(f'#{test_case} 0')
    else:
        # maxi = inject(film, d)
        print(f'#{test_case} {inject(film, d)}')
