#include <stdio.h>

void floyds(int size)
{
    int cntr;
    for(int i =1; i<=size; i++)
    {
        cntr =i;
        for(int j=i; j>0; j--)
        {   
            printf("%3i", cntr++);
        }
        printf("\n");
    }
}

int main(int argc, char *argv[])
{
   floyds(5);
   return 0;

}