def solution(numbers, hand):
    cordi = {1 : [1, 1], 2 : [1, 2], 3 : [1, 3],
             4 : [2, 1], 5 : [2, 2], 6 : [2, 3],
             7 : [3, 1], 8 : [3, 2], 9 : [3, 3],
             '*' : [4, 1], 0 : [4, 2], '#' : [4, 3]}
    answer = ''
    left = "*"
    right = "#"
    for i in numbers:
        if i in [1 ,4, 7]:
            answer += "L"
            left = i
        elif i in[3, 6, 9]:
            answer += "R"
            right = i
        else:
            distanceL = abs(cordi[left][0] - cordi[i][0]) + abs(cordi[left][1] - cordi[i][1])
            distanceR = abs(cordi[right][0] - cordi[i][0]) + abs(cordi[right][1] - cordi[i][1])
            
            if distanceL == distanceR:
                if hand == "right":
                    answer += "R"
                    right = i
                else:
                    answer += "L"
                    left = i
            elif distanceL > distanceR :
                answer += "R"
                right = i
            else:
                answer += "L"
                left = i
                
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
