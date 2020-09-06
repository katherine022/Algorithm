//https://www.acmicpc.net/problem/10026
//적록색약
//C++
//2020.09.06
//skyna

#include<iostream>
#include<string>
#pragma warning(disable:4996)

using namespace std;

int N;
char color[101][101] = { 0 };
int can_visited[101][101] = { 0 }, cannot_visited[101][101] = { 0 };
int can_color = 0, cannot_color = 0;

void dfs(int i, int j, char colors) {
	//cout << "  this point is " << i << " " << j << " " << colors << endl;
	can_visited[i][j] = 1;
	int x[4] = { 1, -1, 0, 0 }; //up, down, right, left
	int y[4] = { 0, 0, 1, -1 }; //up, down, right, left

	for (int k = 0; k < 4; k++) {
		int xpis = i + x[k];
		int ypis = j + y[k];

		if (can_visited[xpis][ypis] == 0 && color[xpis][ypis] == colors) dfs(xpis, ypis, colors);
	}
}

void cannot_dfs(int i, int j) {
	cannot_visited[i][j] = 1;
	//cout << "  this point is " << i << " " << j << " G or R" << endl;
	int x[4] = { 1, -1, 0, 0 }; //up, down, right, left
	int y[4] = { 0, 0, 1, -1 }; //up, down, right, left

	for (int k = 0; k < 4; k++) {
		int xpis = i + x[k];
		int ypis = j + y[k];

		if (cannot_visited[xpis][ypis] == 0 && (color[xpis][ypis] == 'R' || color[xpis][ypis] == 'G')) cannot_dfs(xpis, ypis);
	}
}

void blue_dfs(int i, int j) {
	cannot_visited[i][j] = 1;
	int x[4] = { 1, -1, 0, 0 }; //up, down, right, left
	int y[4] = { 0, 0, 1, -1 }; //up, down, right, left

	for (int k = 0; k < 4; k++) {
		int xpis = i + x[k];
		int ypis = j + y[k];

		if (cannot_visited[xpis][ypis] == 0 && color[xpis][ypis] == 'B' ) blue_dfs(xpis, ypis);
	}
}

void can_color_dfs_all() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (can_visited[i][j] == 0) {
				//cout << "i : " << i << " j : " << j << endl;
				if (color[i][j] == 'R') dfs(i, j, 'R');
				else if (color[i][j] == 'G') dfs(i, j, 'G');
				else dfs(i, j, 'B');

				can_color++;
			}
		}
	}
}

void cannot_color_dfs_all() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (cannot_visited[i][j] == 0) {
				//cout << "i : " << i << " j : " << j << endl;
				if (color[i][j] == 'R' || color[i][j] == 'G') cannot_dfs(i, j);
				else blue_dfs(i, j);

				cannot_color++;
			}
		}
	}
}

int main() {
	cin >> N;
	for (int i = 1; i <= N; i++) {
		scanf("%s", &color[i][1]);
	}

	can_color_dfs_all();
	cannot_color_dfs_all();

	cout << can_color << " " << cannot_color << endl;
}