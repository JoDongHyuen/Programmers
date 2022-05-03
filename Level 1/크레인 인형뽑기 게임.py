def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        
        tmp = 0
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                tmp = board[i][move - 1]
                board[i][move - 1] = 0
                break
        
        if tmp == 0: continue

        if bucket:
            if bucket[-1] == tmp:
                bucket.pop()
                answer += 2
            else:
                bucket.append(tmp)
        else:
            bucket.append(tmp)
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))