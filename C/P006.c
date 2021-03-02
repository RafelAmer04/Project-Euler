#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[]){
    int sol = 0, a = 0, b = 0;
    for(int i = 1;i < 101; i++){
        a += pow(i,2);
        b += i;
    }
    sol = pow(b,2) - a;
    printf("%d\n", sol);
    return 0;
}
