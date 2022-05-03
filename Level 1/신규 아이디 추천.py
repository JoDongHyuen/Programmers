import re

def solution(new_id):
    answer = new_id
    
    # step 1
    answer = answer.lower()
    
    # step 2
    reg = re.compile('[0-9a-z_.\-]')
    answer = reg.findall(answer)
    answer = "".join(answer)
    
    # step 3
    while ".." in answer:
        answer = answer.replace("..", ".")
    
    # step 4
    answer = answer.strip(".")
    
    # step 5
    if answer == '':
        answer = 'a'
    
    # step 6
    answer = answer[0:15]
    if answer[-1] == ".":
        answer = answer[:-1]
        
    # step 7
    while len(answer) < 3:
        answer = answer + answer[-1]
        
    return answer