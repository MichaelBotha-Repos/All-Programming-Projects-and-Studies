#include <stdio.h>

void main()
{   int  i=0;
    char letter = '\'';

    while(i != 7)
    {
        printf("\r%c", letter);
        ++i;
    }

}