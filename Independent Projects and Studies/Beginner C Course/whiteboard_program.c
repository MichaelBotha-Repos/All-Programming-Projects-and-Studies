#include <stdio.h>

int main()
{
    int value;

    printf("Please enter an integer\n");
    scanf("%d", &value);

    printf("variable value = %d\nvariable memory location = %d", value, &value);

    return 0;
}