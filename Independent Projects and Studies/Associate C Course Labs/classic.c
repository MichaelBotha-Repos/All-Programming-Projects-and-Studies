//#include <stdio.h>

void classic(int size)
{
    for(int i =1; i<=size; i++)
    {
        for(int j=i; j>0; j--)
        {
            printf("\\");
        }
        printf("\n");
    }
}

//int main(int argc, char *argv[])
//{
//    classic(5);
//    return 0;

//}
