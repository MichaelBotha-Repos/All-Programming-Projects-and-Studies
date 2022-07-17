#include <stdio.h>

void main()
{
    int counter = 0;
    
    do 
    {
        printf("Fun in the sun\n");
        //counter --;
    }while(counter > 0);

    for(int i = 0; i < 10; i++)
    {
        if(i == 5)continue;
        printf("%i -> in my for loop\n", i);

        if(i == 8)break;

    }

}