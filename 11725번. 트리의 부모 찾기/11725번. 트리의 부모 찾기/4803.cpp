//https://www.acmicpc.net/problem/4803
//트리
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
	int N; //N: 정점의 개수
	int tmp[501][501] = { 0 };
	vector<vector<int>>adj; // 인접리스트  
	vector<bool>visited;
	vector<int>ans1; // 컴포넌트에서의 해당 노드 표시 하기
	vector<int>ans2; // 컴포넌트에서의 해당 간선 수 세기
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
		ans1[num]++; //인접한 노드 수 세기
		for (int next : adj[vertex]) {
			if (!visited[next]) {
				tmp[vertex][next] = true;
				tmp[next][vertex] = true;
				DFS(vertex);
			}
			else {
				if (tmp[vertex][next] == false) {
					ans2[num]++; //vertex -> next로 가는 간선을 안 셌다는 의미가 됨 
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

	vector<int>visited; //방문한 점 리스트

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
			//트리 세기
			if (G.ans1[G.num] == G.ans2[G.num] - 1) cnt++; //컴포넌트의 노드의 수 N이 간선의 개수 N-1을 가질 때 트리로 확정지을 수 있음 
			G.num++;
		}
	}

	cout << cnt << ' ';

}
