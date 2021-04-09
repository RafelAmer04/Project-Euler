#include <stdio.h>

#define ALLOCSIZE 1024
#define free_row(r) row_free(&(r))
#define free_matrix(m) matrix_free(&(m))

typedef struct{
    unsigned int *numbers;
    unsigned int used, reserved;
} row_data;

typedef row_data *row;


typedef struct{
    row *rows;
    unsigned int used, reserved;
} matrix_data;

typedef matrix_data *matrix;



/*
    Create a new row
*/
row new_row();

/*
    Append Space
*/
int append_space(row r);

/*
    Add new number
*/
int add_number(row r, unsigned int n);

/*
    Get number at pos n
*/
unsigned int get_number(row r, unsigned int pos, int *error);

/*
    Add a number at pos n
*/
int add_number_at_pos(row r, unsigned int n, unsigned int pos);

/*
    Free row
*/
void  row_free(row *r);





/*
    Create a new matrix
*/
matrix new_matrix();

/*
    Matrix append space
*/
int matrix_append_space(matrix m);

/*
    Matrix add row
*/
int matrix_add_row(matrix m, row r);

/*
    Matrix get number
*/
unsigned int matrix_get_number(matrix m, unsigned int row, unsigned int col, int *error);

/*
    Free matrix
*/
void matrix_free(matrix *m);

/*
Read File 
*/
matrix matrix_from_file(const char *filename);


