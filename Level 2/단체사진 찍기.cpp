#include <string>
#include <vector>
#include <queue>
#include <cstdlib>
using namespace std;

typedef vector<string> vs;

string friends = "ACFJMNRT";

// 조건 체크하는 함수
bool Condition_Check(string batch, vs data)
{
    int pos1, pos2, distance;
    for (auto condition : data)
    {
        for(int i = 0; i < 8; i++)
        {
            if(condition[0] == batch[i]) pos1 = i;
            if(condition[2] == batch[i]) pos2 = i;
        }
        distance = abs(pos2 - pos1) + '0' - 1;
        
        if (condition[3] == '>') {
            if (distance <= condition[4])
                return false;
        } else if (condition[3] == '<') {
            if (distance >= condition[4])
                return false;
        } else {
            if (distance != condition[4])
                return false;
        }
    }
    
    return true;
}

// 실제 DFS 부분
void DFS_visit(string batch, int* visited, vs data, int* count)
{
    if (batch.size() == 8) {
        int chk = Condition_Check(batch, data);
        if (chk) (*count) += 1;
    } else {
        for (int i = 0; i < 8; i++)
        {
            if (visited[i] == 1) continue;
            visited[i] = 1;
            DFS_visit(batch + friends[i], visited, data, count);
            visited[i] = 0;
            
        }
    }
}

// DFS init
int DFS(string batch, vs data)
{
    int visited[8] = {0};
    int count = 0;
    DFS_visit("", visited, data, &count);
    return count;
}


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vs data) {
    int answer = 0;
    answer = DFS("", data);
    return answer;
}