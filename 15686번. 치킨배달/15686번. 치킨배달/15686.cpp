#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#define ioio() ios_base::sync_with_stdio(0);cin.tie(0)

using namespace std;
int N, M;
int Top = 0, D[13] = { 0 };
int map[51][51] = { 0 };
int dist[14][101] = { 0 };
int ans = 1000000;
vector<pair<int, int>> house;
vector<pair<int, int>> chicken;

void backtracking(int start) {
	if (Top == M) {
		int result = 0;
		for (int i = 0; i < house.size(); i++) {
			int x1 = house[i].first, y1 = house[i].second;
			int m = 10000;
			for (int k = 0; k < M; k++) {
				int j = D[k];
				if (dist[j][i] != 0) {
					m = min(m, dist[j][i]);
					continue;
				}
				int x2 = chicken[j].first, y2 = chicken[j].second;
				dist[j][i] = abs(x1 - x2) + abs(y1 - y2);
				m = min(m, dist[j][i]);
			}
			result += m;
		}
		ans = min(ans, result);
		return;
	}

	for (int i = start; i < chicken.size(); i++) {
		if (chicken.size() - i + 1 < M - Top) break;
		D[Top++] = i;
		backtracking(i + 1);
		Top--;
	}
}

int main() {
	ioio();
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			if (map[i][j] == 1) house.push_back(make_pair(i, j));
			else if (map[i][j] == 2) chicken.push_back(make_pair(i, j));
		}
	}
	
	backtracking(0);
	cout << ans << "\n";
	return 0;
}
