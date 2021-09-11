#include<iostream>
#include<algorithm>

const int MAX = 1000;
using namespace std;

int dp[MAX];

int fibo(int n) {
	if (n < 0) return 0;
	if (dp[n] != -1) return dp[n];
	
	dp[n] = (fibo(n-1) + fibo(n - 2))%10007;
	return dp[n];
}

int main() {
	int n; 
	cin >> n;
	fill(dp, dp+MAX, -1);
	dp[0] = 0;
	cout << fibo(n)%10007;
}