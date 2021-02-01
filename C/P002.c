#include "stdio.h"



int main(){
  int a = 1, b = 2, t, sol = 2;
  while (b <= 4000000) {
    t = a + b;
    a = b;
    b = t;
    if (b % 2 == 0) {
      sol += b;
    }
  }
  printf("%d\n", sol);
  return 0;
}
