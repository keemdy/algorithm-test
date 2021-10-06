def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i, c in enumerate(citations, start = 1):
        if c - i < 0:
            answer = max(answer, c)
        else:
            answer = max(answer, i)
    
    return answer
