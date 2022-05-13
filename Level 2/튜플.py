def solution(s):
    answer = []
    temp = s[2:-2].split("},{")
    temp = sorted(temp , key = lambda x: len(x))
    for elements in temp:
        element = elements.split(",")
        for e in element:
            if e in answer: continue
            answer.append(e)

    return list(map(int, answer))

########################################################
# 다른 사람 풀이법                                      #
# 정규식 써서 분해한 다음에 카운팅함                     #
# 가장 많이 카운팅 된 숫자 순으로 리스트에 추가하면 됨    #
########################################################
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter