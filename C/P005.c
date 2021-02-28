#include <stdio.h>

unsigned int GCD(unsigned int n1,unsigned int n2){
    if((n1 == 0) || (n2 == 0))
        return 0;
    while(n2 != 0){
        unsigned int r = n1 % n2;
        n1 = n2;
        n2 = r;
    }
    return n1;
    
}


int main(int argc, char const *argv[]){
    unsigned int sol = 1;
    for (unsigned int i = 1; i < 21; i++){
        unsigned int gcd = GCD(i, sol);
        sol *= i / gcd;
    }
    printf("%u\n", sol);
    return 0;
}
    