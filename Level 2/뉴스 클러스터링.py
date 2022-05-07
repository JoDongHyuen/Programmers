import re

def solution(str1, str2):
    answer = 0
    
    str1_set = []
    str2_set = []
    numerator = 0
    dinominator = 0
    r = re.compile('[a-z][a-z]')
    
    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2].lower()
        if r.match(tmp):
            str1_set.append(tmp)
        
    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2].lower()
        if r.match(tmp):
            str2_set.append(tmp)
    
    for i in range(len(str1_set)):
        for j in range(len(str2_set)):
            if str1_set[i] == str2_set[j]:
                str2_set[j] = " "
                numerator += 1
                break
    
    #######################################################
    # 다중집합이라도 n(합집합) = n(A) + n(B) - n(교집합) 임 #
    #######################################################
    if str1_set or str2_set:
        dinominator = len(str1_set) + len(str2_set) - numerator
        answer = int(numerator / dinominator * 65536)
    else:
        answer = 65536
        
    return answer