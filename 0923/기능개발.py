def solution(progresses, speeds):
    answer = []
    compare = []
    n = len(progresses)
    
    for i in range(n):
        check = 100 - progresses[i]
        if not (check % speeds[i]):
            compare.append(check // speeds[i])
        else:
            compare.append(check // speeds[i] + 1)
            
    cnt = 1
    flag = [False] * n

    for i in range(n):
        if flag[i]: continue
        for j in range(i+1, n):
            if compare[i] >= compare[j]:
                flag[j] = True
                cnt += 1
            else:
                break
        answer.append(cnt)
        cnt = 1
        
    return answer
