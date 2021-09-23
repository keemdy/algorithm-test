import heapq

def solution(jobs):
    answer, start, now, i = 0, -1, 0, 0
    q = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q, (job[1], job[0]))
        if q:
            cost, current_time = heapq.heappop(q)
            start = now
            now += cost
            answer += (now - current_time)
            i += 1
        else:
            now += 1
    
    return (answer // len(jobs))
