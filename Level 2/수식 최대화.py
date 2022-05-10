from collections import deque
import re

def DFS_visit(operator, operand, visited, now):
    if sum(visited) == 3:
        global answer
        if abs(int(operand[0])) > answer:
            answer = abs(int(operand[0]))
    else:
        if visited[now] == False:
            visited[now] = True
            if now == 0:
                operator_tmp, operand_tmp = multiply(operator, operand)
            elif now == 1:
                operator_tmp, operand_tmp = plus(operator, operand)
            else:
                operator_tmp, operand_tmp = minus(operator, operand)
            
            for i in range(3):
                DFS_visit(operator_tmp, operand_tmp, visited, i)
            visited[now] = False
        

def DFS(operator, operand, visited):
    for i in range(3):
        DFS_visit(operator, operand, visited, i)

def plus(operator, operand):
    operator_tmp = deque(operator)
    operand_tmp = deque(operand)
    operator_result = deque()
    operand_result = deque()
    
    while operator_tmp:
        if operator_tmp[0] == '+':
            tmp1 = operand_tmp.popleft()
            tmp2 = operand_tmp.popleft()
            operator_tmp.popleft()
            operand_tmp.appendleft(tmp1 + tmp2)
        else:
            operator_result.append(operator_tmp.popleft())
            operand_result.append(operand_tmp.popleft())
    
    if operand_tmp:
        operand_result.append(operand_tmp.popleft())
        
    return operator_result, operand_result
    

def minus(operator, operand):
    operator_tmp = deque(operator)
    operand_tmp = deque(operand)
    operator_result = deque()
    operand_result = deque()
    
    while operator_tmp:
        if operator_tmp[0] == '-':
            tmp1 = operand_tmp.popleft()
            tmp2 = operand_tmp.popleft()
            operator_tmp.popleft()
            operand_tmp.appendleft(tmp1 - tmp2)
        else:
            operator_result.append(operator_tmp.popleft())
            operand_result.append(operand_tmp.popleft())
    
    if operand_tmp:
        operand_result.append(operand_tmp.popleft())
        
    return operator_result, operand_result
    
def multiply(operator, operand):
    operator_tmp = deque(operator)
    operand_tmp = deque(operand)
    operator_result = deque()
    operand_result = deque()
    
    while operator_tmp:
        if operator_tmp[0] == '*':
            tmp1 = operand_tmp.popleft()
            tmp2 = operand_tmp.popleft()
            operator_tmp.popleft()
            operand_tmp.appendleft(tmp1 * tmp2)
        else:
            operator_result.append(operator_tmp.popleft())
            operand_result.append(operand_tmp.popleft())
    
    if operand_tmp:
        operand_result.append(operand_tmp.popleft())
        
    return operator_result, operand_result

def solution(expression):
    global answer
    answer = 0
    visited = [False for _ in range(3)]
    p = re.compile('[*+-]')
    q = re.compile('[0-9]+')
    operator = p.findall(expression)
    operand = q.findall(expression)
    operand = list(map(int, operand))
    
    DFS(operator, operand, visited)
    
    return answer

# 다른사람 풀이
# 순서대로 split한 다음 괄호를 씌운 다시 join 후에 eval로 연산 진행하는 방법임
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

print(solution("100-200*300-500+20"))