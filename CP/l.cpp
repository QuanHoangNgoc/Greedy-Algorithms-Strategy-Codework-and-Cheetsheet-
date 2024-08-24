#include <bits/stdc++.h>
#define fi first
#define se second
#define int long long
#define str string
using namespace std;
template <typename T>
void cerrprint(T v) {
  for (auto x : v) cerr << x << ", ";
  cerr << endl;
}

vector<str> splitStr(str text) {
  stringstream ss(text);
  str word;
  vector<str> words;
  while (ss >> word) {
    words.push_back(word);
  }
  return words;
}
int findIndex(vector<str> texts, str pattern, int begin) {
  for (int i = begin; i < (int)texts.size(); ++i)
    if (texts[i] == pattern) return i;
  return -1;
}

int32_t main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  freopen("A.inp", "r", stdin);

  str text = "", s = "";
  while (cin >> s) {
    text += s + " ";
  }
  // cerr << text << endl;

  vector<str> texts = splitStr(text);
  // cerrprint(texts);
  vector<str> patterns = splitStr("Welcome Hue University of Sciences");
  // cerrprint(patterns);

  bool check = true;
  int id = 0;
  for (auto pattern : patterns) {
    id = findIndex(texts, pattern, 0);
    if (id == -1) {
      check = false;
      break;
    }
  }

  if (check)
    cout << "Yes";
  else
    cout << "No";

  return 0;
}

/*
Welcome Hue city
Hue is the capital of Thua Thien
Hue province
University of Hue
of my life
Sciences scientific fields
or scientific disciplines
*/
