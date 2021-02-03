//https://www.acmicpc.net/problem/1904
//01타일
//2020,02.03
//C++
//skyna

#include<iostream>
#include<algorithm>

const int MAX = 1000001;
using namespace std;

int dp[MAX];

int fibo(int n) {
	if (n == 1) return 1;
	if (n == 2) return 2;
	if (dp[n] != 0) return dp[n];

	dp[n] = (fibo(n - 1) + fibo(n - 2)) % 15746;
	return dp[n];
}

int main() {
	int n;
	cin >> n;
	fill(dp, dp + MAX, 0);
	dp[0] = 1;
	cout << fibo(n);
}
