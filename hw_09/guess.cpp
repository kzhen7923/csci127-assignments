#include <iostream>

int main() {
  int number;
  int high = 99;
  int low = 0;
  int response;
  int guess = (high + low)/2;
  std::cout << "Input a number between 0-99 ";
  std::cin >> number;

  std::cout << "Is " << guess << " your number? Respond with -1,0 or 1 ";
  std::cin >> response;

  while (response != 0) {
    if (response == 1) {
      high = guess;
    }
    else {
      low = guess;
    }
    guess = (low + high)/2;

    std::cout << "Is " << guess << " your number? Respond with -1,0, or 1";
    std::cin >> response;
  }
  std::cout << guess << " is the correct number!"<< std::endl;
  return 0;
 }
