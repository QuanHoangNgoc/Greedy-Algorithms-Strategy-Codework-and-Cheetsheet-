#include <bits/stdc++.h>
#define fi first
#define se second
#define int long long
using namespace std;

map<int, int> d;
map<int, int> dmax;
map<int, int> ddiff;
void pttsnt(int n, map<int, int> &d) {
  for (int i = 2; 1ll * i * i <= n; ++i) {
    if (n == 1) break;
    if (n % i != 0) continue;
    while (n % i == 0) {
      d[i]++;
      n /= i;
    }
  }

  if (n > 1) d[n]++;
}
int POW(int a, int b) {
  int res = 1;
  for (int i = 1; i <= b; ++i) res *= a;
  return res;
}

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  // freopen("A.inp", "r", stdin);

  int A, B, C, D;
  cin >> A >> B >> C >> D;
  pttsnt(A, d);
  pttsnt(C, dmax);
  pttsnt(D, ddiff);

  int rate = 1e9 + 1;
  for (auto it = dmax.begin(); it != dmax.end(); ++it) {
    int x = (*it).first;
    if (dmax[x] <= ddiff[x]) continue;
    int tmp = rate;
    rate = min(rate, (long long)POW(x, ddiff[x] - d[x] + 1));
    if ((A * rate) % B == 0) {
      rate = tmp;
    }
  }

  int X = A * rate;
  if (C % X == 0 && D % X != 0 && X % B != 0)
    cout << X;
  else
    cout << -1;

  return 0;
}