def solution(N, number):
    answer = 0
    dp = [[] for i in range(9)]
    if N == number:
        return 1
    
    for i in range(1, 9):
        dp[i].append(int(str(N)*i))
    
    for i in range(2, 9):
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].append(a + b)
                    dp[i].append(a - b)
                    dp[i].append(a*b)
                    if b != 0:
                        dp[i].append(a//b)
        if number in dp[i]:
            return i
        dp[i] = list(set(dp[i]))
    # print(dp)
    return -1
