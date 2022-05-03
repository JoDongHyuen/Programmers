# 숫자 카운트가 10, 100을 넘어서 2 ~ 3자리가 되는 걸 검사해야함!

def solution(s):
    answer = 1001
    
    # 길이가 1일 때, 예외 처리
    if len(s) == 1:
        return 1
    
    # len(s//2) 했다가 틀림
    # 반례 : abab 하면 2자리 패턴은 그냥 스킵됨
    # 범위 신경 안써서 생긴 일
    for i in range(1, len(s)//2 + 1):
        tmp = i
        # 같은 패턴을 세는 변수
        count = 1
        for j in range(i, len(s), i):
            
            if s[j : j + i] == s[j - i : j]:
                count += 1
            else:
                if count > 1:
                    # 카운트가 10^n 넘어가면 자리수가 n개 되는거 생각 못 했음
                    tmp += len(str(count))
                # tmp 부분 그냥 tep += i 했다가 틀림
                # 반례 : abcabcdede 하면 마지막 ded 랑 e 비교하고
                # e길이 만큼 1 더해야하는데 3 더해져버림
                tmp += len(s[j:j+i])
                count = 1         
        
        # 이부분 넣은 이유, 마지막에 연속 인정되면 추가 처리하기 위해서임
        # 이부분 없을 시 반례 : aaaaaaaa
        if count > 1:
            tmp += len(str(count))
    
        answer = min(tmp, answer)

    return answer

print(solution('abcabcdede'))