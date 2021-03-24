#include <stdio.h>
#include <readnumbers.h>

#define EAST 0
#define SOUTH 1
#define SOUTHEAST 3
#define NORTHEAST 4


unsigned int get_product(matrix m, unsigned int row, unsigned int col, unsigned int n, int dir, int *error){
    if(dir == EAST){

    }

}


int main(int argc, char *argv[]){
    matrix m;
    if((m = matrix_from_file("P011.txt")) == NULL){
        printf("error reading file \n");
        return 1;
    }


    unsigned int sol;
    unsigned int p;


    
    for(unsigned int x = 0; x < 17; x++){
        for(unsigned int y = 0; y < 17; y++){
            int error;

            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x,y+1,&error) * matrix_get_number(m,x,y+2,&error) * matrix_get_number(m,x,y+3,&error);
            if(error){
                printf("Can't multiply 1  X= %u Y= %u\n", x,y);
                return 1;
            }
            if(p > sol)
                sol = p;
            
            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x+1,y+1,&error) * matrix_get_number(m,x+2,y+2,&error) * matrix_get_number(m,x+3,y+3,&error);
            if(error){
                printf("Can't multiply 2\n");
                return 1;
            }
            if(p > sol)
                sol = p;
            
            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x+1,y,&error) * matrix_get_number(m,x+2,y,&error) * matrix_get_number(m,x+3,y,&error);
            if(error){
                printf("Can't multiply 3\n");
                return 1;
            }
            if(p > sol)
                sol = p;

        }
    }

    for(unsigned int x = 16; x < 20; x++){
        for(unsigned int y = 0; y < 17;y++){
            int error;

            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x,y+1,&error) * matrix_get_number(m,x,y+2,&error) * matrix_get_number(m,x,y+3,&error);
            if(error){
                printf("Can't multiply 4\n");
                return 1;
            }
            if(p > sol)
                sol = p;

            p = matrix_get_number(m,y,x,&error) * matrix_get_number(m,y+1,x,&error) * matrix_get_number(m,y+2,x,&error) * matrix_get_number(m,y+3,x,&error);
            if(error){
                printf("Can't multiply 5\n");
                return 1;
            }
            if(p > sol)
                sol = p;
            
        }
    }

    for(unsigned int x = 19; x > 3;x--){
        for(unsigned int y = 0; y < 17; y++){
            int error;

            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x-1,y+1,&error) * matrix_get_number(m,x-2,y+2,&error) * matrix_get_number(m,x-3,y+3,&error);
            if(error){
                printf("Can't multiply 6\n");
                return 1;
            }
            if(p > sol)
                sol = p;
        }
    }

    free_matrix(m);
    printf("The solution is: %u\n", sol);


    return 0;
}