#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define ALLOCSIZE 1024

char *digitsFromFile(const char *filename)
{
  /*
    Open the file
  */
	FILE *fp;
	if ((fp = fopen(filename, "r")) == NULL)
		return NULL;
  /*
    Local variables
  */
	int c;
	char *str, *new;
	size_t alloc_size = ALLOCSIZE, str_size = 0;
	if ((str = (char *)calloc(alloc_size,sizeof(char))) == NULL)
		return NULL;
  /*
    Read the file
  */
  while ((c = getc(fp)) != EOF)
  {
    if (!isdigit(c))
      continue;
    if (str_size == alloc_size - 1)
    {
			alloc_size += ALLOCSIZE;
			if ((new = (char *)realloc(str,alloc_size * sizeof(char))) == NULL)
      {
        free(str);
				return NULL;
      }
      str = new;
		}
    str[str_size++] = c;
  }
	str[str_size] = '\0';
  /*
    Close the file and return the value
  */
  fclose(fp);
	return str;
}



int main(int argc, char const *argv[]){
    char *data;
    if((data = digitsFromFile("P008.txt")) == NULL){
        printf("Error!\n");
        return 1;
    }
    size_t len = strlen(data);
    unsigned long int p = 1;
    unsigned long int sol = 0;

    for (int i = 0; i < len; i++){
        p = 1;
        for (int j = 0; j < 13; j++){
            p *= data[i+j] - '0';
        }
        if (p > sol){
            sol = p;
        }
    }
    printf("%lu\n", sol);
    return 0;
}