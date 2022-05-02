def solution(id_list, report, k):
    answer = []
    
    report = set(report)
    crime = {}
    result = {}
    
    for element in report:
        A, B = element.split(" ")
        if B in crime:
            crime[B].append(A)
        else:
            crime[B] = [A]
    
    for element in crime:
        if len(crime[element]) < k:
            continue
            
        for user in crime[element]:
            if user in result:
                result[user] = result[user] + 1
            else:
                result[user] = 1

    for user in id_list:
        if user in result:
            answer.append(result[user])
        else:
            answer.append(0)

    return answer


# 잘 푼 사람 코드
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer