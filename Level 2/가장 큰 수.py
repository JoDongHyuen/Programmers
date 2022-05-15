def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    print(numbers)
    answer = str(int("".join(numbers)))
    
    return answer

print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0,0,0,0]))