//#include<iostream>
//#include<cmath>
//#include<algorithm>
//
//using namespace std;
//const int MAX = 100001;
//
//int N;
//int dp[MAX];
//int sqnum[MAX];
//
//int sumSquare(int n, int sum) {
//	if (sum < 1) return 0;
//	if (n == 0) return 0;
//	if (dp[sum] > 0) return dp[sum];
//
//	if (sqnum[n] == 0) sqnum[n] = n * n;
//	int result = sumSquare(n - 1, sum);
//	if (n*n <= sum) result = min(result, sumSquare(n - 1, sum - sqnum[n])+1,sumSquare(n, sum - sqnum[n])+1);
//	
//	dp[sum] = result;
//	return result;
//}
//
//int main() {
//	cin >> N;
//	int num = int(sqrt(N));
//	cout << sumSquare(num, N);
//}