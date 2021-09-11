//https://www.acmicpc.net/problem/4803
//Ʈ��
//C++
//2021.04.10
//skyna

#include<iostream>
#include<algorithm>
#pragma warning (disable:4996)
#include<vector>
#include<queue>

using namespace std;

class Graph {
public :
	int N; //N: ������ ����
	int tmp[501][501] = { 0 };
	vector<vector<int>>adj; // ��������Ʈ  
	vector<bool>visited;
	vector<int>ans1; // ������Ʈ������ �ش� ��� ǥ�� �ϱ�
	vector<int>ans2; // ������Ʈ������ �ش� ���� �� ����
	int num;

	Graph() : N(0) {
	}
	Graph(int n) : N(n) { 
		adj.resize(N + 1); 
		ans1.resize(N + 1, 0);
		ans2.resize(N + 1, 0);
		num = 1;
	}

	void addEdge(int u, int v) {
		adj[u].push_back(v);
		adj[v].push_back(u);
	}

	void sortList() {
		for (int i = 0; i < N; i++) {
			sort(adj[i].begin(), adj[i].end());
		}
	}

	void DFS(int vertex){
		visited[vertex] = true;
		ans1[num]++; //������ ��� �� ����
		for (int next : adj[vertex]) {
			if (!visited[next]) {
				tmp[vertex][next] = true;
				tmp[next][vertex] = true;
				DFS(vertex);
			}
			else {
				if (tmp[vertex][next] == false) {
					ans2[num]++; //vertex -> next�� ���� ������ �� �ôٴ� �ǹ̰� �� 
					tmp[vertex][next] = true;
					tmp[next][vertex] = true;
				}
			}
		}
	}
};

int main() {
	int N, M;
	int a, b;
	int cnt = 0;

	vector<int>visited; //�湮�� �� ����Ʈ

	scanf("%d %d", &N, &M);
	getchar();

	Graph G(N);

	for (int i = 0; i < M; i++) {
		scanf("%d %d", &a, &b);
		G.addEdge(a, b);
	}
	G.sortList();
	
	for (int i = 1; i < N + 1; i++) {
		if (!G.visited[i]) {
			G.DFS(i);
			//Ʈ�� ����
			if (G.ans1[G.num] == G.ans2[G.num] - 1) cnt++; //������Ʈ�� ����� �� N�� ������ ���� N-1�� ���� �� Ʈ���� Ȯ������ �� ���� 
			G.num++;
		}
	}

	cout << cnt << ' ';

}
