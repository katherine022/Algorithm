//https://www.acmicpc.net/problem/2193
//
//C++
//2021.02.02
//skyna

#include<cstdio>
#include<algorithm>
#pragma warning(disable:4996)

using namespace std;
const int MAX = 91;
int N;
long long dp[MAX][2];

long long maketwo(int len, int digit) {
	if (len < 1) return 0;
	if (dp[len][digit] != -1) return dp[len][digit];

	long long result = 0;
	if (digit == 1) result = maketwo(len - 1, 0);
	else result = maketwo(len - 1, 1) + maketwo(len - 1, 0);

	dp[len][digit] = result;
	return result;
}

int main() {
	scanf("%d", &N);
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <=2; j++) {
			dp[i][j] = -1;
		}
	}

	dp[1][0] = 1;
	dp[1][1] = 1;
	printf("%lld\n", maketwo(N, 1));
}
