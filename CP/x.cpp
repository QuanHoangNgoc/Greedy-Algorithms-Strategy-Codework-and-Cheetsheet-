#include <bits/stdc++.h>
#include <unistd.h>

int main() {
  int a = 0;
  if (CreateProcess() == 0) {
    a = a + 5;
    std::cout << a << " " << &a << std::endl;
  } else {
    a = a - 5;
    std::cout << a << " " << &a << std::endl;
  }
}