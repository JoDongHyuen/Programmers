def solution(N, stages):
    answer = []
    rate = []
    count = {i : 0 for i in range(1, N + 1)}
    total = len(stages)

    for stage in stages:
        if stage in count:
            if stage <= N:
                count[stage] += 1
    
    for i in range(1, N + 1):
        if total == 0:
            rate.append([0, i])
            continue
        rate.append([count[i] / total, i])
        total -= count[i]
    rate.sort(key=lambda x: (-x[0], x[1]))
    
    for ra, st in rate:
        answer.append(st)
        
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# tmp.sort(key=lambda x: (x[0], -x[1]))