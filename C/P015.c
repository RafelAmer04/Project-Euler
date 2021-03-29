#include <stdio.h>


unsigned long int binomial(unsigned int n, unsigned int k){
    unsigned int m;
    m = k>(n-k)? k: n-k;
    unsigned long int a = 1;
    for(unsigned int i = m+1; i <= n; i++){
        a *= i;
        a /= i-m;
    }
    return a;
}

int main(int argc, char *argv[]){
    unsigned long int sol = binomial(150,50);
    printf("%lu\n", sol);
}