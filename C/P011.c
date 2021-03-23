#include <stdio.h>
#include <readnumbers.h>


int main(int argc, char *argv[]){
    matrix m;
    if((m = matrix_from_file("P011.txt")) == NULL){
        printf("Error reading file \n");
        return 1;
    }
}