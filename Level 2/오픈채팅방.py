def solution(record):
    answer = []
    
    dict = {}
    
    for message in record:
        words = message.split()
        
        if words[0] == "Enter":
            dict[words[1]] = words[2]
        elif words[0] == "Change":
            dict[words[1]] = words[2]
    
    for message in record:
        words = message.split()
        
        if words[0] == "Enter":
            answer.append(dict[words[1]] + "님이 들어왔습니다.")
        elif words[0] == "Leave":
            answer.append(dict[words[1]] + "님이 나갔습니다.")
            
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

