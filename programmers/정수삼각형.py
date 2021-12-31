def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [c for c in triangle]

    for r in range(1, n):
        for c in range(r+1):
            right, left = 0, 0
            if r == c:
                right = dp[r-1][c-1]
            elif c == 0: 
                left = dp[r-1][c]
            else:
                right, left = dp[r-1][c], dp[r-1][c-1]
            
            dp[r][c] = max(left, right) + dp[r][c]
            
    return max(dp[-1])