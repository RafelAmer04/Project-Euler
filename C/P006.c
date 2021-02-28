#include <stdio.h>

int power(int x, int n){
    int sol = 1;
    for (int i = 0; i < n; i++){
        sol *= x;
    }
    return sol;
}

int main(int argc, char const *argv[]){
    int sol = 0, a = 0, b = 0;
    for(int i = 1;i < 101; i++){
        a += power(i,2);
        b += i;
    }
    sol = power(b,2) - a;
    printf("%d\n", sol);
    return 0;
}
