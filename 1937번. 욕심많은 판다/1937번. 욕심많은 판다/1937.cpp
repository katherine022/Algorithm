//https://www.acmicpc.net/problem/1937
//øÂΩ…¿Ô¿Ã ∆«¥Ÿ
//C++
//2021.01.05
//skyna

#include<iostream>
#pragma warning(disable : 4996)

using namespace std;

int start_x, start_y;
int n, max = 0;
int bamboo[501][501] = { 0 };
int visited[501][501] = { 0 };

int dfs(int x, int y) {
	int day = 1;
	visited[x][y] = 1;
	cout << "node " << bamboo[x][y] << " visited" << endl;
	int direct_x[4] = { 0, 0, 1, -1 };
	int direct_y[4] = { 1, -1, 0, 0 };

	for (int i = 0; i < 4; i++) {
		int di_x = x + direct_x[i];
		int di_y = y + direct_y[i];
		if (bamboo[di_x][di_y] > bamboo[x][y] && visited[di_x][di_y] == 0) day += dfs(di_x, di_y);
	}
	return day;
}

void dfs_all() {
	int day = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cout << "-- new DFS begins --" << endl;
			day = dfs(i, j);
			if (max < day) max = day;
			memset(visited, 0, sizeof(visited));
		}
	}
}

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			scanf("%d", &bamboo[i][j]);
		}
	}
	dfs_all();
	cout << max;
}