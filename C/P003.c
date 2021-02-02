#include "stdio.h"

int main(int argc, char const *argv[]){
  unsigned long int n = 600851475143;
  int d = 2;
  while(n > 1){
    if (n % d == 0) {
      n /= d;
    } else {
      d += 1;
    }
  }
  printf("%d\n", d);
}
