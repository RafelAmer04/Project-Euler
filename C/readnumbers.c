#include <readnumbers.h>
#include <stdlib.h>
#include <ctype.h>

row new_row(){
    row r;
    if((r = (row)malloc(sizeof(row_data))) == NULL)
        return NULL;

    r->used = 0;
    if ((r->numbers = (unsigned int *)malloc(ALLOCSIZE*sizeof(unsigned int))) == NULL){
        free(r);
        return NULL;
    }
    r->reserved = ALLOCSIZE;
    return r;
}

int append_space(row r){
    r->reserved += ALLOCSIZE;
    unsigned int *new;
    if((new = (unsigned int *)realloc(r->numbers,r->reserved * sizeof(unsigned int))) == NULL){
        printf("Realloc error. Elements reserved: %u\n",r->reserved);
        free(r->numbers);
        r->numbers = NULL;
        return -1;
    }
    r->numbers = new;
    return 0;
}

int add_number(row r, unsigned int n){
    if(r->used == r->reserved)
        if(append_space(r) < 0)
            return -1;
    r->numbers[r->used] = n;
    r->used++;
    return 0;
}

unsigned int get_number(row r, unsigned int pos, int *error){
    if(pos >= r->used){
        *error = 1;
        return 0;
    }
    *error = 0;
    return r->numbers[pos];
}

int add_number_at_pos(row r, unsigned int n, unsigned int pos){
    if(pos >= r->reserved){
        r->reserved = pos+ALLOCSIZE;
        unsigned int *new;
        if((new = (unsigned int *)realloc(r->numbers,r->reserved * sizeof(unsigned int))) == NULL){
            printf("Realloc error. Elements reserved: %u\n",r->reserved);
            free(r->numbers);
            r->numbers = NULL;
            return -1;
        }
        r->numbers = new;
    }
    r->numbers[pos] = n;
    if (pos >= r->used)
        r->used = pos+1;
    return 0;
}

void row_free(row *r){
    if(*r == NULL)
        return;
    if((*r)->numbers != NULL){
        free((*r)->numbers);
        (*r)->numbers = NULL;
    }
    free(*r);
    *r = NULL;
}



matrix new_matrix(){
    matrix m;
    if((m = (matrix)malloc(sizeof(matrix_data))) == NULL)
        return NULL;

    m->used = 0;
    if ((m->rows = (row *)malloc(ALLOCSIZE*sizeof(row))) == NULL){
        free(m);
        return NULL;
    }
    m->reserved = ALLOCSIZE;
    return m;
}

int matrix_append_space(matrix m){
    m->reserved += ALLOCSIZE;
    row *new;
    if((new = (row *)realloc(m->rows,m->reserved * sizeof(row))) == NULL){
        printf("Realloc error. Rows eserved: %u\n",m->reserved);
        free(m->rows);
        m->rows = NULL;
        return -1;
    }
    m->rows = new;
    return 0;
}

int matrix_add_row(matrix m, row r){
    if(m->used == m->reserved)
        if(matrix_append_space(m) < 0)
            return -1;
    m->rows[m->used] = r;
    m->used++;
    return 0;
}

unsigned int matrix_get_number(matrix m, unsigned int row, unsigned int col, int *error){
    if(row >= m->used){
        *error = 1;
        return 0;
    }
    return get_number(m->rows[row], col, error);
}

void matrix_free(matrix *m){
    if(*m == NULL)
        return;

    if((*m)->rows != NULL){
        for(unsigned int i = 0; i < (*m)->used; i++){
            free_row((*m)->rows[i]);
            (*m)->rows[i] = NULL;
        }
    }
    free((*m)->rows);
    free(*m);
    *m = NULL;
}


matrix matrix_from_file(const char *filename){
    matrix m;
    if((m = new_matrix()) == NULL) {
        printf("Couldn't create new matrix\n");
        return NULL;
    }

    row r;
    if((r = new_row()) == NULL) {
      printf("Couldn't create the first row\n");
      free_matrix(m);
      return NULL;
    }


    FILE *fp;
	if ((fp = fopen(filename, "r")) == NULL)
		return NULL;

    int c;
    char temp[32];
    int used = 0;


    while ((c = getc(fp)) != EOF){
        if((c == '0') && (used == 0))
            continue;

        if(isdigit(c))
            temp[used++] = c;

        if((used > 0) && ((c == ' ') || (c == '\n'))){
            temp[used] = '\0';
            char *p;
            unsigned int n = strtoul(temp, &p, 10);
            if(add_number(r, n) < 0) {
                printf("Couldn't add number to row %u\n", m->used);
                free_row(r);
                free_matrix(m);
                return NULL;
            }
            used = 0;
        }
        if(c == '\n'){
            if(matrix_add_row(m, r) < 0) {
                printf("Couldn't add row to matrix\n");
                free_matrix(m);
                return NULL;
            }
            if((r = new_row()) == NULL) {
                printf("Couldn't create a new row\n");
                free_matrix(m);
                return NULL;
            }
        }   
    }
    if((r != NULL) && (r->used > 0)){
        if(matrix_add_row(m, r) < 0) {
                printf("Couldn't add row to matrix\n");
                free_matrix(m);
                return NULL;
        }
    }
    fclose(fp);
    return m;
}

