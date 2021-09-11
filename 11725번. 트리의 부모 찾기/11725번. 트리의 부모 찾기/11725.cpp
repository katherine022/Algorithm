////https://www.acmicpc.net/problem/11725
////트리의 부모 찾기
////C++
////2020.09.12
////skyna
//#include<iostream>
//#include<algorithm>
//#pragma warning (disable:4996)
//#include<vector>
//#include<queue>
//
//using namespace std;
//
//int N;
//vector<vector<int>> w;
//vector<int> parent;
//
//void bfs() {
//	vector<bool> visited(N+1, false);
//	queue<int> q;
//
//	q.push(1);
//	visited[1] = true;
//
//	while (!q.empty()) {
//		int curr = q.front();
//		q.pop();
//		for (int next : w[curr]) {
//			if (!visited[next]) {
//				visited[next] = true;
//				parent[next] = curr;
//				q.push(next);
//			}
//		}
//	}
//}
//
//
//int main() {
//	
//	int a, b;
//	scanf("%d", &N);
//
//	w.resize( N+1 );
//	parent.resize(N + 1);
//	
//	for (int i = 0; i < N-1; i++) {
//		scanf("%d %d", &a, &b);
//		w[a].push_back(b);
//		w[b].push_back(a);
//	}
//
//	bfs();
//	for (int i = 2; i <= N; i++) {
//		printf("%d\n", parent[i]);
//	}
//}