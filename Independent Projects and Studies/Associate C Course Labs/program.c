#include <stdio.h>
#include <errno.h>
#include <string.h>

int main()
{
    FILE *program_file, *new_file;
    char program[1000][128];
    int cntr =0;

    // Open existing stream to existing program 
    program_file = fopen("C:\\Users\\Michael Botha\\Documents\\GitHub\\All-Programming-Projects-and-Studies\\Independent Projects and Studies\\Associate C Course Labs\\program.c", "r");
    if(program_file == NULL)
    {
        printf("Unable to open existing program file:\n%s", strerror(errno));
        return 1;
    }

    // Open stream for editted text file
    new_file = fopen("C:\\Users\\Michael Botha\\Documents\\GitHub\\All-Programming-Projects-and-Studies\\Independent Projects and Studies\\Associate C Course Labs\\program2.c", "w+");
    if(new_file == NULL)
    {
        printf("Unable to create new text file");
        return 1;
    }


    while(fgets(&(program[cntr][0]), 128, program_file) != NULL)
    {
        cntr++;

    }

    cntr=0;
    while(program[cntr][0] != 0)
    {

        fprintf(new_file, "%i %s", cntr+1, &(program[cntr][0]));
        cntr++;
    }

    fclose(program_file);
    fclose(new_file);
    
    return 0;
}