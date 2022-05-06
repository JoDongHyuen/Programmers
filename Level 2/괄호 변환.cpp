#include <string>
#include <vector>
#include <iostream>
using namespace std;

typedef vector<char> vc;

string incorrect(string u)
{
	string tmp;
	if (u.size() > 2) {
		tmp = u.substr(1, u.size() - 2);
		for (int i = 0; i < tmp.size(); i++)
		{
			if (tmp[i] == '(') tmp[i] = ')';
			else tmp[i] = '(';
		}
		return "(" + tmp + ")";
	}
	else return "()";
}

string logic(string p)
{
	int operandL = 0;
	int operandR = 0;
	string u = "";
	string v;
	vc q;

	for (int i = 0; i < p.size(); i++)
	{
		if (p[i] == '(') {
			operandL += 1;
			u += "(";
			q.emplace_back('(');
		}
		else {
			operandR += 1;
			u += ")";
			if (q.empty() || q.back() != '(') q.emplace_back(')');
			else q.pop_back();
		}

		if (operandL == operandR && operandL != 0)
		{
			v = p.substr(i + 1);
			if (q.empty()) return u + logic(v);
			else return incorrect(u) + logic(v);
		}
	}

	return "";
}

string solution(string p) {
	string answer = "";
	answer = logic(p);
	cout << answer << "\n";
	return answer;
}

int main()
{
	solution("()))((()");
}


// 다른 사람 풀이
#include <bits/stdc++.h>
using namespace std;

//****************************************//
// check 하는 부분 간단하게 r변수 써서 음수 체크한 거 GOOD
// 나는 vector를 스택처럼 사용해서 했었음...
//****************************************//
bool check(const string &a) {
    int r = 0;
    for (char ch : a) {
        if (ch == '(') ++r;
        else --r;
        if (r < 0) return false;
    }
    return r == 0;
}
string solution(string p) {
    if (p == "") return "";
    if (check(p)) return p;

    //****************************************//
    // t 변수 하나로 처리한 점 GOOD
    // 나는 변수 2개 선언해서 했었음
    // 마지막에 if (t==0) 넣은거도 GOOD
    //****************************************//
    int i, t = 0;
    for (i = 0; i < p.size(); ++i) {
        if (p[i] == '(') ++t;
        else --t;
        if (t == 0) break;
    }

    string u = p.substr(0, i + 1);
    string v = p.substr(i + 1);

    if (check(u)) return u + solution(v);

    for (char &ch : u) ch = ch == '(' ? ')' : '(';
    return string("(") + solution(v) + ")" + u.substr(1, u.size() - 2);
}
