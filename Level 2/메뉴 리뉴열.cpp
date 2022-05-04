#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

typedef map<string, int> msi;
typedef vector<int> vi;

msi result;
// 이거 생각 못해서 마지막 부분 고민 많이 했었음
int max_count[11];


void DFS_visit(int now, string menus, string order, vi course)
{
    menus += order[now];
    if (find(course.begin(), course.end(), menus.length()) != course.end())
    {
        if(result.find(menus) != result.end())
            result[menus] += 1;
        else
            result[menus] = 1;
        if (result[menus] > max_count[menus.length()])
            max_count[menus.length()] = result[menus];
    }
    for (int i = now + 1; i < order.length(); i++)
        DFS_visit(i, menus, order, course);
}
void DFS(string order, vi course)
{
    for (int i = 0; i < order.length(); i++)
    {
        DFS_visit(i, "", order, course);    
    }
}

vector<string> solution(vector<string> orders, vi course) {
    cin.tie(0);
    ios::sync_with_stdio(false);
    vector<string> answer;
    string tmp;
    
    for (auto order : orders)
    {
        sort(order.begin(), order.end());
        DFS(order, course);
    }
    
    for (auto test : result)
        if (test.second == max_count[(test.first).length()])
            if(test.second != 1)
                answer.emplace_back(test.first);
    
    return answer;
}