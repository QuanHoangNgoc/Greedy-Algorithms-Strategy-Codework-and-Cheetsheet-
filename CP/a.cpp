#include <bits/stdc++.h>
#define fi first
#define se second
#define int long long
#define str string
using namespace std;

const int N = 100;
int number;
struct Process {
  string name;
  int arrivalTime;
  int burstTime;
  int priority;
} processes[N];

bool cmp(Process &x, Process &y) { return x.arrivalTime < y.arrivalTime; }

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  // freopen("A.inp", "r", stdin);

  cout << "number is :" << endl;
  cin >> number;
  for (int i = 0; i < number; ++i) {
    cout << "process " << i << ": " << endl;
    cout << "name: " << endl;
    cin >> processes[i].name;
    cout << "arrival time: " << endl;
    cin >> processes[i].arrivalTime;
    cout << "burst time: " << endl;
    cin >> processes[i].burstTime;
    cout << "priority: " << endl;
    cin >> processes[i].priority;
    cout << endl;
  }

  sort(processes + 0, processes + number, cmp);

  priority_queue<pair<int, int>> q;
  for (int i = 0; i < number; ++i) {
    q.push({i, processes[i].burstTime});
  }

  return 0;
}
