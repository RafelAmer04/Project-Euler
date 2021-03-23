#include <stdio.h>
#include <readnumbers.h>


int main(int argc, char *argv[]){
    matrix m;
    if((m = matrix_from_file("P011.txt")) == NULL){
        printf("error reading file \n");
        return 1;
    }


    unsigned int sol;
    unsigned int p;





    row r;
    r = m->rows[m->used-1];
    for(unsigned int i = 0; i < r->used; i++)
        printf("%u ",r->numbers[i]);

    printf("\n");
  



    printf("Number of rows in file: %u\n", m->used);
    free_matrix(m);
    





    for(unsigned int x = 0; x < 16; x++){
        for(unsigned int y = 0; y < 16; y++){
            int error;

            p = matrix_get_number(m,x,y,&error) * matrix_get_number(m,x,y+1,&error) * matrix_get_number(m,x,y+2,&error) * matrix_get_number(m,x,y+3,&error);
            if(error){
                printf("Can't multiply 1 %u\n", error);
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


    return 0;
}