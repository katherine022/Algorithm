//https://www.acmicpc.net/problem/2573
//빙산
//C++
//2020.09.06
//skyna

#include<iostream>
#include<cstring>
#pragma warning(disable:4996)

using namespace std;

int N, M;
int ice[301][301] = { 0 };
int melting_ice[301][301] = { 0 };
int visited[301][301] = { 0 };

void melting() {
	int zero = 0;
	int x[4] = { 0, 0, 1, -1 };
	int y[4] = { 1, -1, 0, 0 };

	for (int i = 1; i < N - 1; i++) {
		for (int j = 1; j < M - 1; j++) {
			for (int k = 0; k < 4; k++) {
				int xpis = i + x[k];
				int ypis = j + y[k];

				if (ice[xpis][ypis] == 0) zero++;
			}

			melting_ice[i][j] = ice[i][j] - zero;
			if (melting_ice[i][j] < 0) melting_ice[i][j] = 0;
			zero = 0;
		}
	}

	memcpy(ice, melting_ice, sizeof(melting_ice));
	for (int i = 0; i < N; i++) {
		memset(melting_ice[i], 0, sizeof(int) * M); //¸ðµç °ª 0À¸·Î ÃÊ±âÈ­
	}	
}

void dfs(int i, int j) {
	visited[i][j] = 1;

	int x[4] = { 0, 0, 1, -1 }; //right, left, up, down
	int y[4] = { 1, -1, 0, 0 }; //right, left, up, down

	for (int k = 0; k < 4; k++) {
		int xpis = i + x[k];
		int ypis = j + y[k];

		if (visited[xpis][ypis] == 0 && ice[xpis][ypis] > 0) dfs(xpis, ypis);
	}
}

int dfs_all() {
	int components = 0;
	
	for (int i = 1; i < N - 1; i++) {
		for (int j = 1; j < M - 1; j++) {
			if (visited[i][j] == 0 && ice[i][j] > 0) {
				dfs(i, j);
				components++;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		memset(visited[i], 0, sizeof(int) * M);
	}
	return components;
}

int main() {
	int island = 0;
	int time = 0;
	cin >> N >> M;

	for (int i = 0; i < N ; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &ice[i][j]);
		}
	}

	while (1) {
		melting();
		island = dfs_all();
		if (island == 0) {
			time = 0;
			break;
		}
		else if (island == 1) time++;
		else if (island >= 2) {
			time++;
			break;
		}
	}

	cout << time << endl;
}