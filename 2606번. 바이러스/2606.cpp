//https://www.acmicpc.net/problem/2606
// 바이러스 
// C++
// 2020.09.05
// skyna

#include<iostream>

using namespace std;

int N;
int lines; 
int computer[101][101] = { 0 };
int visited[101] = { 0 }; 
int virus = 0;

void dfs(int a) {
	//cout << "this point is " << a << endl;
	visited[a] = 1;
	if (a != 1) virus++;

	for (int i = 1; i <= N; i++) {
		if (visited[i] == 0 && computer[a][i] == 1) {
			dfs(i);
		}
	}
}

int main() {
	int a, b; 
	cin >> N;
	cin >> lines;

	for (int i = 0; i < lines; i++) {
		cin >> a >> b;
		computer[a][b] = computer[b][a] = 1;
	}

	dfs(1);
	
	cout << virus;
}