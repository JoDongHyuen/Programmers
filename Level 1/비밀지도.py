def solution(n, arr1, arr2):
    answer = [[" " for _ in range(n)] for __ in range(n)]
    tmp = '0' + str(n) + 'b'
    for i in range(n):
        binary = format(arr1[i], tmp)
        for j in range(n):
            if binary[j] == '1':
                answer[i][j] = "#"
    
    for i in range(n):
        binary = format(arr2[i], tmp)
        for j in range(n):
            if binary[j] == '1':
                answer[i][j] = "#"
    
    for i in range(n):
        answer[i] = "".join(answer[i])
        
    return answer