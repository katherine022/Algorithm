////https://www.acmicpc.net/problem/1991
////트리 순회
////C++
////2021.04.10
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
//vector<char> parent;
//vector<char> lc, rc;
//
//
////전위순회
//void preorder(int r) {
//	char a = r + 64;
//	cout << a;
//	if (lc[r] != '.' && lc[r] != 0) preorder(lc[r]-64);
//	if (rc[r] != '.' && rc[r] != 0) preorder(rc[r]-64);
//}
//
////중위순회
//void inorder(int r) {
//	char a = r + 64;
//	if (lc[r] != '.' && lc[r] != 0) inorder(lc[r]-64);
//	cout << a;
//	if (rc[r] != '.' && rc[r] != 0) inorder(rc[r]-64);
//}
//
//
////후위순회
//void postorder(int r) {
//	char a = r + 64;
//	if (lc[r] != '.' && lc[r] != 0) postorder(lc[r]-64);
//	if (rc[r] != '.' && rc[r] != 0) postorder(rc[r]-64);
//	cout << a;
//}
//
//int main() {
//	
//	char p, l, r;
//	scanf("%d\n", &N);
//
//	parent.resize(N + 1, 0);
//	lc.resize(N + 1, 0);
//	rc.resize(N + 1, 0);
//	
//	for (int i = 0; i < N-1; i++) {
//		scanf("%c %c %c", &p, &l, &r);
//		getchar();
//
//		if (l != '.') parent[l - 64] = p;
//		if (r != '.') parent[r - 64] = p;
//		lc[p - 64] = l;
//		rc[p - 64] = r;
//	}
//
//	preorder(1);
//	cout << endl;
//	inorder(1);
//	cout << endl;
//	postorder(1);
//	cout << endl;
//}