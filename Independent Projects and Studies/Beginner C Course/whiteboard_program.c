#include <stdio.h>

void main()
{
    int* p, val = 10;

    p = &val;

    printf("%i --> %i", p, *p);



}