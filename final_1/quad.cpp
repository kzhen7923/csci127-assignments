#include <math.h>
#include <iostream>

int discriminant(int a,int b,int c)
{
  int num;
  num = ((b * b) - (4 * a * c));
  return num;
}

double quadsolve(int a, int b, int c)
{
  int discrim;
  discrim = discriminant(a,b,c);
  double root;
  if (discrim >= 0) {
    root = (-b + sqrt(discrim)) / ( 2 * a);
    return root;
  }
  else {
    return 0;
  }
}


int main()
{
  std::cout << "Discriminant( 1,10,6)= " << discriminant(1,10,6) << "\n";
  std:: cout << "Discriminant (5,2,3) = " << discriminant (5,2,3) << "\n";

  std::cout << "quadsolve ( 1,10,6) = " << quadsolve(1,10,6) << "\n";
  std::cout << "quadsolve ( 5,2,3) = " << quadsolve(5,2,3) << "\n";
  return 0;
  
}
