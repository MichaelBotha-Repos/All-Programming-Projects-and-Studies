#include <stdio.h>
#define test 1##2-2

int main()
{
    int x =

    #ifdef test
        1
    #else
        2
    #endif
    ;

    printf("%i %i", x, test);

    return 0;
}