#include <stdio.h>
#include <readnumbers.h>


int main(int argc, char *argv[]){
    matrix m;
    if((m = matrix_from_file("P011.txt")) == NULL){
        printf("Error reading file \n");
        return 1;
    }


    unsigned int sol;
    unsigned int p;

    for(unsigned int x; x < 18; x++){
        for(unsigned int y; y < 18; y++){
            
        }
    }



    return 0,
}