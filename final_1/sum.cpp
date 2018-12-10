#include <iostream>

int sumofsquares(int a, int b) {
  int i;
  int sum = 0;
  int square;
  for (i = a; i <= b; i++) {
    square = i * i;
    sum = sum  + square;
  }
  std::cout << "Sum = " << sum  << "\n";
  return sum;
}


int main() {
  int result;
  result = sumofsquares(1,3);
  std::cout << "1^2 + 2^2 + 3^2 = " << result << "\n";
  return 0;
}


