#include "stdio.h"

int main() {
  int sol = 0;
  for (int i = 0; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0)
      sol += i;
  }
  printf("%d\n", sol);
  return 0;
}
