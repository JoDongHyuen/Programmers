################
#시간 초과 풀이 #
################
def solution(number, k):
    temp, answer = number[:k], number[k:]
    for i in range(len(answer)):
        if not temp:
                break
        value = max(temp)
        if value < answer[i]:
            break
        temp = temp + answer[i]
        answer = answer[:i] + str(value) + answer[i + 1:]
        idx = temp.find(value)
        temp = temp[idx + 1:]
        if (temp == temp[idx + 1:]): break

    return answer

###############################
# stack 사용해서 O(n)으로 해결 #
###############################
def solution(number, k):
    stk = []
    check = 0
    length = len(number) - k
    
    for num in number:
        if check >= k:
            stk.append(num)
        else:
            if not stk:
                stk.append(num)
            else:
                if stk[-1] < num:
                    while stk[-1] < num:
                        stk.pop()
                        check += 1
                        if check >= k : break
                        if not stk: break
                    stk.append(num)
                else:
                    stk.append(num)
    stk = "".join(stk)
    
    # 987654321, 3 같은 예제 처리하기 위함
    if len(stk) > length:
        stk = stk[:length]
    
    return stk

print(solution("987654321", 3))
