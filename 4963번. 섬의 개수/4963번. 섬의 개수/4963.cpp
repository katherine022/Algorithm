// https://www.acmicpc.net/problem/4963
// 섬의 개수
// C++
// 2020.09.05
// skyna
#include<iostream>
#include<cstring>
#pragma warning(disable : 4996)
using namespace std;

int island[52][52] = { 0 };
int visited[52][52] = { 0 };
int a = 0, b = 0;

void dfs(int i, int j) {
	visited[i][j] = 1;

	int x[8] = { 0, 0, 1, -1, -1, -1, 1, 1}; //left, right, up, down, diag_left_up, diag_right_up, diag_left_down, diag_right_down
	int y[8] = { -1, 1, 0, 0, -1, 1, -1, 1}; //left, right, up, down, diag_left_up, diag_right_up, diag_left_down, diag_right_down

	for (int k = 0; k < 8; k++) {
		int xpis = i + x[k];
		int ypis = j + y[k];
		if (visited[xpis][ypis] == 0 && island[xpis][ypis] == 1) dfs(xpis, ypis);
	}
}

void dfs_all() {
	int island_num = 0;

	for (int i = 1; i <= a; i++) {
		for (int j = 1; j <= b; j++) {
			if (visited[i][j] == 0 && island[i][j] == 1) {
				dfs(i, j);
				island_num++;
			}
		}
	}
	
	cout << island_num << endl;
}

int main() {
	while (1) {
		cin >> b >> a;
		if (a == 0 && b == 0) break;
		for (int i = 1; i <= a; i++) {
			for (int j = 1; j <= b; j++) {
				scanf("%d", &island[i][j]);
			}
		}

		dfs_all();
		for (int i = 0; i <= 51; i++) {
			memset(island[i], 0, sizeof(int) * 51);
		}
		memset(visited, 0, sizeof(visited));
	}
}