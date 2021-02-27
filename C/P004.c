#include <stdio.h>
#include <string.h>

int IsPalindrome(int num){
    char pal[10];
    sprintf(pal,"%d", num);
    int len = strlen(pal);
    for(int i = 0;i < len/2; i++){
        if (pal[i] != pal[len-i-1])
            return 0;   
    }
    return 1;
}

int main(int argc, char const *argv[]){
    int max = 0;
    for(int a = 100; a < 1000; a++){
        for(int b = a; b < 1000; b++){
            int product = a * b;
            if(IsPalindrome(product) && (product > max)) 
                max = product;
         }
    }
    printf("The maximum palindrome is: %d\n", max);
    return 0;
}

