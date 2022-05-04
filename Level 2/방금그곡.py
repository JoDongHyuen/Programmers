def solution(m, musicinfos):
    answer = ['']
    
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", "f")
    m = m.replace("G#", "g")
    m = m.replace("A#", "a")
    
    for musicinfo in musicinfos:
        start, end, name, tune = musicinfo.split(",")
        start_hour, start_minute = map(int, start.split(":"))
        end_hour, end_minute = map(int, end.split(":"))
        total = (end_hour - start_hour) * 60 + end_minute - start_minute
        
        tune = tune.replace("C#", "c")
        tune = tune.replace("D#", "d")
        tune = tune.replace("F#", "f")
        tune = tune.replace("G#", "g")
        tune = tune.replace("A#", "a")
        
        repeat = total // len(tune) + 1
        target = tune * repeat
        target = target[:total]
        
        if m in target:
            if answer[0] == '':
                answer = [name, total]
            elif answer[1] < total:
                answer = [name, total]
                
    
    if answer[0] == '':
        answer = ["(None)"]
    return answer[0]