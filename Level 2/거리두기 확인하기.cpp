#include <iostream>
#include <string>
#include <vector>
using namespace std;

int dx[12] = { 0, 1, 0, -1, 0, 2, 0, -2, 1, 1, -1, -1 };
int dy[12] = { 1, 0, -1, 0, 2, 0, -2, 0, 1, -1, 1, -1 };

int check(int x, int y, vector<string> place)
{
	int nx, ny;
	int i;

	for (i = 0; i < 4; i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || nx > 5) continue;
		if (ny < 0 || ny > 5) continue;
		if (place[nx][ny] != 'P') continue;

		return 0;
	}

	for (i = 4; i < 8; i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || nx > 5) continue;
		if (ny < 0 || ny > 5) continue;
		if (place[nx][ny] != 'P') continue;
		if (place[x + dx[i] / 2][y + dy[i] / 2] == 'X') continue;

		return 0;
	}

	for (i = 8; i < 12; i++)
	{
		nx = x + dx[i];
		ny = y + dy[i];

		if (nx < 0 || nx > 5) continue;
		if (ny < 0 || ny > 5) continue;
		if (place[nx][ny] != 'P') continue;
		if (place[x + dx[i]][y] == 'X' && place[x][y + dy[i]] == 'X') continue;

		return 0;
	}

	return 1;
}

vector<int> solution(vector<vector<string>> places) {
	vector<int> answer;

	int i, j, k;
	int checker;
	for (auto place : places)
	{
		cout << "---------\n";
		checker = 1;
		for (i = 0; i < 5; i++)
		{
			for (j = 0; j < 5; j++)
			{
				if (place[i][j] == 'P')
					checker = check(i, j, place);
				if (checker == 0)
				{
					cout << i << " " << j << "\n";
					break;
				}
			}
			if (checker == 0) break;
		}
		answer.emplace_back(checker);
	}
	return answer;
}

int main()
{
	vector<vector<string>> places;
	vector<string> temp;
	temp.emplace_back("POOOP");
	temp.emplace_back("OXXOX");
	temp.emplace_back("OPXPX");
	temp.emplace_back("OOXOX");
	temp.emplace_back("POXXP");

	places.emplace_back(temp);

	solution(places);

}