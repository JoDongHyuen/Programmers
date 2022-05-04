def to_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            mod = chr(65 + mod % 10)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, t, m, p):
    
    answer = ''
    
    number_list = '0'
    
    now = 1
    while len(answer) < t:
        number_list += to_n(now, n)
        now += 1
        
        while len(number_list) > p:
            answer += number_list[p - 1]
            p += m
    
    return answer