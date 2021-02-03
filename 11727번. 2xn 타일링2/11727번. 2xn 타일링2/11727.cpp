//https://www.acmicpc.net/problem/11727
//2xn 타일링2
//2020.02.03
//c++
//skyna

#include<iostream>
#include<algorithm>

const int MAX = 1001;
using namespace std;

int dp[MAX];

int fibo(int n) {
	if (n == 1) return 1;
	if (dp[n] != 0) return dp[n];
	
	dp[n] = (fibo(n-1) + 2*fibo(n - 2))%10007;
	return dp[n];
}

int main() {
	int n; 
	cin >> n;
	fill(dp, dp+MAX, 0);
	dp[0] = 1;
	cout << fibo(n);
}