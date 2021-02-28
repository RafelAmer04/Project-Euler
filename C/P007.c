#include <stdio.h>
#include <math.h>

int IsPrime(int p){
    float q = sqrt(p);
    if (p % 2 == 0){
        return 0;
    }
    int i = 3;
    while (i <= q){
        if (p  % i == 0){
            return 0;
        }
        i += 2; 
    }
    return 1;
}

int main(int argc, char const *argv[]){
    int j = 1, p = 0;
    while (p < 10001){
        if (IsPrime(j)){
            p +=1;
        }
        j += 1;
    }
    printf("%d\n", j);
    return 0;
}
