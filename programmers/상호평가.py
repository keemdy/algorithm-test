def check_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'
def solution(scores):
    answer = ''
    n = len(scores)
    transpose = [[] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in scores:
            transpose[cnt].append(j[i])
        cnt += 1

    for i in range(n):
        print(transpose[i])
        sum_score = sum(transpose[i])
        sum_cnt = n
        max_score_index = transpose[i].index(max(transpose[i]))
        min_score_index = transpose[i].index(min(transpose[i]))
        if i == max_score_index or i == min_score_index:
            if transpose[i].count(transpose[i][i]) == 1:
                print(i, max_score_index, min_score_index)
                sum_cnt -= 1
                sum_score -= transpose[i][i]
        answer += check_grade(sum_score/sum_cnt)
            
    return answer