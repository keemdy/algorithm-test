def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0]*3
    for i, ans in enumerate(answers):
        if first[i%len(first)] == ans:
            score[0] += 1
        if second[i%len(second)] == ans:
            score[1] += 1
        if third[i%len(third)] == ans:
            score[2] += 1
    return [i + 1 for i, s in enumerate(score) if s == max(score)]
