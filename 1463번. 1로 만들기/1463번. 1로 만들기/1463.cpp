//#include<iostream>
//#include<algorithm>
//
//const int MAX = 1000001;
//using namespace std;
//
//int dp[MAX];
//
//int makeone(int n) {
//	if (n == 1) return 0;
//	if (dp[n] != -1) return dp[n];
//	
//	int result = makeone(n - 1) + 1;
//	if (n % 3 == 0) result = min( result, makeone(n / 3) + 1 );
//	if (n % 2 == 0) result = min( result, makeone(n / 2) + 1 );
//	dp[n] = result;
//	return result;
//}
//
//int main() {
//	int n; 
//	cin >> n;
//	fill(dp, dp+MAX, -1);
//	cout << makeone(n);
//}