import re
def solution(dartResult):
    answer = 0
    record = [0, 0, 0]
    m = re.compile('[0-9]+.[*#]?')
    s = re.compile('[0-9]+')
    points = m.findall(dartResult)
    
    for i in range(3):
        point = s.findall(points[i])
        record[i] = int(point[0])
        if 'D' in points[i]:
            record[i] **= 2
        elif 'T' in points[i]:
            record[i] **= 3
        
        if '*' in points[i]:
            record[i] *= 2
            if i != 0:
                record[i - 1] *= 2
        elif '#' in points[i]:
            record[i] *= -1
        
    answer = sum(record)

    return answer

print(solution('1S2D*3T'))