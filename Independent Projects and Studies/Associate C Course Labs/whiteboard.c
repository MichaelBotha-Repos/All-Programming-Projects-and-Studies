#include <stdio.h>
#include <string.h>

int main()
{
    char names[][90] = {
                            "The Way Love Should be",
                            "Bad Wrap",
                            "Terrible Moods"
                        };
    char *names2[] = {
                            "The Way Love Should be",
                            "Bad Wrap",
                            "Terrible Moods"
                        };

    **(names + 10) = 'A';

    printf("%s  \n%s", names[0], names2[0]);


    return 0;
}